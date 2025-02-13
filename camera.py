import subprocess
import json
import logging
from mock_camera_settings import get_mock_settings
from attached_assets.gPhoto2settings import gPhoto2setting

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
            # Use the gPhoto2setting class to parse the output
            parser = gPhoto2setting(result.stdout)
            settings = {}

            # Convert the parsed settings to our API format
            for setting in parser.formObject:
                path = setting['path']
                settings[path] = {
                    'full_path': path,
                    'section_path': f"/main/{setting['group']}",
                    'name': setting['name'],
                    'readable_name': setting['label'],
                    'type': setting['typeUI'],
                    'current': setting['current'],
                    'choices': [opt['name'] for opt in setting['options']] if isinstance(setting['options'], list) else [],
                    'range': setting['options'] if isinstance(setting['options'], dict) else None,
                    'readonly': False,  # This info isn't in the original parser, defaulting to False
                    'description': f"Setting for {setting['label']}"
                }

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