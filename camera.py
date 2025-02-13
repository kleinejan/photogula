import subprocess
import json
import logging

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
        result = subprocess.run(['gphoto2', '--list-all-config'],
                              capture_output=True, text=True)
        settings = parse_gphoto_settings(result.stdout)
        return settings
    except Exception as e:
        logging.error(f"Camera settings error: {str(e)}")
        return {}

def parse_gphoto_settings(output):
    settings = {}
    current_setting = None
    
    for line in output.split('\n'):
        if line.startswith('/main/'):
            current_setting = {
                'name': line.split('/')[-1],
                'type': None,
                'current': None,
                'choices': []
            }
            settings[current_setting['name']] = current_setting
        elif line.startswith('Type:'):
            if current_setting:
                current_setting['type'] = line.split(':')[1].strip()
        elif line.startswith('Current:'):
            if current_setting:
                current_setting['current'] = line.split(':')[1].strip()
        elif line.startswith('Choice:'):
            if current_setting:
                choice = line.split(':')[1].strip()
                current_setting['choices'].append(choice)
    
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
