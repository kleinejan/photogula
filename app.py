import os
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import camera
import utils
import logging

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "timelapse_secret_key"

# Configure database
database_url = os.environ.get("DATABASE_URL")
if not database_url:
    logging.error("DATABASE_URL environment variable is not set")
    raise RuntimeError("DATABASE_URL must be set")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
db.init_app(app)

@app.route('/')
def dashboard():
    system_info = utils.get_system_info()
    camera_status = camera.get_camera_status()
    return render_template('dashboard.html', system_info=system_info, camera_status=camera_status)

@app.route('/capture')
def capture():
    camera_settings = camera.get_camera_settings()
    # Get current settings from database
    settings_config = db.session.query(models.CameraSettings).first()
    enabled_settings = []
    intervals = {'day': 300, 'night': 600}

    if settings_config:
        enabled_settings = settings_config.enabled_settings or []
        intervals = {
            'day': settings_config.day_interval,
            'night': settings_config.night_interval
        }

    return render_template('capture.html', 
                         settings=camera_settings,
                         enabled_settings=enabled_settings,
                         intervals=intervals)

@app.route('/preview')
def preview():
    page = request.args.get('page', 1, type=int)
    images = utils.get_captured_images(page)
    return render_template('preview.html', images=images, page=page)

@app.route('/system')
def system():
    return render_template('system.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/api/camera/enabled-settings', methods=['POST'])
def update_enabled_settings():
    try:
        data = request.json
        enabled_settings = data.get('enabled_settings', [])

        settings_config = db.session.query(models.CameraSettings).first()
        if not settings_config:
            settings_config = models.CameraSettings(
                name="Default",
                enabled_settings=enabled_settings
            )
            db.session.add(settings_config)
        else:
            settings_config.enabled_settings = enabled_settings

        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        logging.error(f"Error updating enabled settings: {str(e)}")
        return jsonify({"success": False, "error": str(e)})

@app.route('/api/camera/toggle', methods=['POST'])
def toggle_capture():
    status = camera.toggle_capture()
    return jsonify({"status": status})

@app.route('/api/camera/settings', methods=['POST'])
def update_settings():
    try:
        data = request.json
        day_settings = data.get('day_settings', {})
        night_settings = data.get('night_settings', {})

        settings_config = db.session.query(models.CameraSettings).first()
        if not settings_config:
            settings_config = models.CameraSettings(
                name="Default",
                settings_day=day_settings,
                settings_night=night_settings
            )
            db.session.add(settings_config)
        else:
            settings_config.settings_day = day_settings
            settings_config.settings_night = night_settings

        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        logging.error(f"Error updating settings: {str(e)}")
        return jsonify({"success": False, "error": str(e)})

with app.app_context():
    import models
    db.create_all()