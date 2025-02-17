import subprocess
import logging
from datetime import datetime
from attached_assets.gPhoto2settings import gPhoto2setting
from extensions import db
from models import CameraSettings

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
        # Run gphoto2 with debugging enabled to get detailed output
        result = subprocess.run(['gphoto2', '--debug', '--list-all-config'],
                              capture_output=True, text=True, env={'LANG': 'C'})
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

            if not settings:
                raise Exception("No settings found in camera output")

            # Store settings in database
            settings_config = db.session.query(CameraSettings).first()
            if not settings_config:
                settings_config = CameraSettings(
                    name="Default",
                    camera_config=settings,
                    last_config_update=datetime.utcnow()
                )
                db.session.add(settings_config)
            else:
                settings_config.camera_config = settings
                settings_config.last_config_update = datetime.utcnow()

            db.session.commit()
            return settings
        else:
            # If no camera is connected or there's an error, raise exception
            raise Exception(f"Error getting camera settings: {result.stderr}")
    except Exception as e:
        logging.error(f"Camera settings error: {str(e)}")
        raise RuntimeError(f"Failed to get camera settings: {str(e)}")

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