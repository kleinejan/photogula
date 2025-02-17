import os
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import camera
import utils
import logging
from datetime import datetime, time
from sqlalchemy import and_

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
    try:
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
    except Exception as e:
        logging.error(f"Error accessing camera: {str(e)}")
        return render_template('error.html', 
                             error="Could not access camera settings. Please check if the camera is properly connected.",
                             details=str(e))

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

@app.route('/schedules')
def schedules():
    """View all schedules"""
    schedules = db.session.query(models.ScheduledSettings).all()
    camera_settings = db.session.query(models.CameraSettings).all()
    return render_template('schedules.html', 
                         schedules=schedules, 
                         camera_settings=camera_settings,
                         today=datetime.now())

@app.route('/api/schedules', methods=['POST'])
def create_schedule():
    """Create a new schedule"""
    try:
        data = request.json
        if not data.get('name'):
            return jsonify({"success": False, "error": "Name is required"}), 400

        # Convert date and time strings to Python objects
        try:
            start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
            start_time = datetime.strptime(data['start_time'], '%H:%M').time()
            end_time = datetime.strptime(data['end_time'], '%H:%M').time()
        except ValueError as e:
            return jsonify({"success": False, "error": "Invalid date or time format"}), 400

        # Validate date and time
        if start_date > end_date:
            return jsonify({"success": False, "error": "End date must be after start date"}), 400

        if start_time >= end_time:
            return jsonify({"success": False, "error": "End time must be after start time"}), 400

        # Create schedule
        schedule = models.ScheduledSettings(
            name=data['name'],
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            day_interval=data.get('day_interval', 300),
            night_interval=data.get('night_interval', 600),
            is_active=True
        )

        db.session.add(schedule)
        db.session.commit()
        return jsonify({"success": True, "message": "Schedule created successfully"})
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating schedule: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/schedules/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    """Update an existing schedule"""
    try:
        schedule = db.session.query(models.ScheduledSettings).get(schedule_id)
        if not schedule:
            return jsonify({"success": False, "error": "Schedule not found"}), 404

        data = request.json
        if 'start_date' in data:
            schedule.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
        if 'end_date' in data:
            schedule.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
        if 'start_time' in data:
            schedule.start_time = datetime.strptime(data['start_time'], '%H:%M').time()
        if 'end_time' in data:
            schedule.end_time = datetime.strptime(data['end_time'], '%H:%M').time()
        if 'days_of_week' in data:
            schedule.days_of_week = data['days_of_week']
        if 'interval_seconds' in data:
            schedule.interval_seconds = data['interval_seconds']
        if 'is_active' in data:
            schedule.is_active = data['is_active']
        if 'name' in data:
            schedule.name = data['name']
        if 'camera_settings_id' in data:
            schedule.camera_settings_id = data['camera_settings_id']

        db.session.commit()
        return jsonify({"success": True, "message": "Schedule updated successfully"})
    except Exception as e:
        logging.error(f"Error updating schedule: {str(e)}")
        return jsonify({"success": False, "error": str(e)})


with app.app_context():
    import models
    db.create_all()