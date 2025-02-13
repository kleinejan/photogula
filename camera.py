import subprocess
import json
import logging
from mock_camera_settings import get_mock_settings

def get_camera_status():
    try:
        result = subprocess.run(['gphoto2', '--auto-detect'], 
                              capture_output=True, text=True)
        if "Found" in result.stdout:
            return {"connected": True, "message": result.stdout}
        return {"connected": False, "message": "No camera detected"}
    except Exception as e:
        logging.error(f"Camera status error: {str(e)}")
        return {"connected": False, "message": str(e)}

def get_camera_settings():
    try:
        # First try to get real camera settings
        result = subprocess.run(['gphoto2', '--list-all-config'],
                              capture_output=True, text=True)
        logging.debug(f"Camera settings output: {result.stdout}")
        if result.returncode == 0 and result.stdout.strip():
            settings = parse_gphoto_settings(result.stdout)
            if settings:  # If we got settings successfully
                return settings
            logging.warning("No settings found in camera output, falling back to mock settings")
            return get_mock_settings()
        else:
            # If no camera is connected or there's an error, return mock settings
            logging.info("Using mock camera settings")
            return get_mock_settings()
    except Exception as e:
        logging.error(f"Camera settings error: {str(e)}, falling back to mock settings")
        return get_mock_settings()

def parse_gphoto_settings(output):
    settings = {}
    current_path = None
    current_setting = None

    for line in output.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('/main/'):
            # New setting found
            current_path = line.split()[0]  # Get path before any spaces
            current_setting = {
                'full_path': current_path,
                'section_path': '/'.join(current_path.split('/')[:-1]),
                'name': current_path.split('/')[-1],
                'readable_name': current_path.split('/')[-1].replace('_', ' ').title(),
                'type': None,
                'current': None,
                'choices': [],
                'range': None,
                'readonly': False,
                'description': ''
            }
            settings[current_path] = current_setting

        elif current_setting and ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().lower()
            value = value.strip()

            if key == 'label':
                current_setting['readable_name'] = value
            elif key == 'type':
                if 'RANGE' in value:
                    current_setting['type'] = 'RANGE'
                elif 'TOGGLE' in value:
                    current_setting['type'] = 'TOGGLE'
                elif 'RADIO' in value or 'MENU' in value:
                    current_setting['type'] = 'MENU'
                else:
                    current_setting['type'] = 'TEXT'
            elif key == 'current':
                current_setting['current'] = value
            elif key.startswith('choice'):
                # Extract the actual value from choices like "0 On" or "1 Off"
                choice_value = value.split(' ', 1)[-1] if ' ' in value else value
                current_setting['choices'].append(choice_value)
            elif key == 'bottom':
                if not current_setting['range']:
                    current_setting['range'] = {}
                current_setting['range']['min'] = value
            elif key == 'top':
                if not current_setting['range']:
                    current_setting['range'] = {}
                current_setting['range']['max'] = value
            elif key == 'step':
                if not current_setting['range']:
                    current_setting['range'] = {}
                current_setting['range']['step'] = value
            elif key == 'readonly':
                current_setting['readonly'] = value.lower() == 'yes'
            elif key in ['help', 'info', 'printable']:
                if not current_setting['description']:  # Only set if not already set
                    current_setting['description'] = value

    return settings

def toggle_capture():
    try:
        # Implementation would depend on how you want to handle
        # the capture process (background task, etc.)
        return {"success": True, "status": "Capture toggled"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def update_settings(settings):
    try:
        for setting, value in settings.items():
            cmd = ['gphoto2', '--set-config', f'{setting}={value}']
            subprocess.run(cmd, check=True)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}