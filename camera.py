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
        if result.returncode == 0:
            settings = parse_gphoto_settings(result.stdout)
            return settings
        else:
            # If no camera is connected or there's an error, return mock settings
            logging.info("Using mock camera settings")
            return get_mock_settings()
    except Exception as e:
        logging.error(f"Camera settings error: {str(e)}, falling back to mock settings")
        return get_mock_settings()

def parse_gphoto_settings(output):
    settings = {}
    current_setting = None
    current_section = None

    for line in output.split('\n'):
        line = line.strip()
        if not line:
            continue

        if line.startswith('/main/'):
            # Extract section and setting name
            parts = line.split('/')
            if len(parts) >= 3:
                section = parts[2].split()[0]  # Get section name before any spaces
                setting_name = parts[-1].split()[0]  # Get last part before any spaces

                # Create a readable name for the setting
                readable_name = setting_name.replace('_', ' ').title()

                current_setting = {
                    'name': setting_name,
                    'section': section,
                    'readable_name': readable_name,
                    'type': None,
                    'current': None,
                    'choices': [],
                    'range': None,
                    'readonly': False,
                    'description': ''
                }
                settings[setting_name] = current_setting

        elif current_setting:
            if line.startswith('Label:'):
                current_setting['readable_name'] = line.split(':', 1)[1].strip()
            elif line.startswith('Type:'):
                type_value = line.split(':', 1)[1].strip()
                if 'RANGE' in type_value:
                    current_setting['type'] = 'RANGE'
                elif 'RADIO' in type_value or 'MENU' in type_value:
                    current_setting['type'] = 'MENU'
                else:
                    current_setting['type'] = 'TEXT'
            elif line.startswith('Current:'):
                current_setting['current'] = line.split(':', 1)[1].strip()
            elif line.startswith('Choice:'):
                choice = line.split(':', 1)[1].strip()
                current_setting['choices'].append(choice)
            elif line.startswith('Bottom:'):
                if not current_setting['range']:
                    current_setting['range'] = {}
                current_setting['range']['min'] = line.split(':', 1)[1].strip()
            elif line.startswith('Top:'):
                if not current_setting['range']:
                    current_setting['range'] = {}
                current_setting['range']['max'] = line.split(':', 1)[1].strip()
            elif line.startswith('Step:'):
                if not current_setting['range']:
                    current_setting['range'] = {}
                current_setting['range']['step'] = line.split(':', 1)[1].strip()
            elif line.startswith('Readonly:'):
                current_setting['readonly'] = line.split(':', 1)[1].strip().lower() == 'yes'
            elif line.startswith('Help:') or line.startswith('Info:'):
                current_setting['description'] = line.split(':', 1)[1].strip()

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