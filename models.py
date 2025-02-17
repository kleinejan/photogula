from extensions import db
from datetime import datetime

class CameraSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    day_interval = db.Column(db.Integer, default=300)  # 5 minutes
    night_interval = db.Column(db.Integer, default=600)  # 10 minutes
    location = db.Column(db.String(100))
    enabled_settings = db.Column(db.JSON)  # List of enabled setting names
    settings_day = db.Column(db.JSON)
    settings_night = db.Column(db.JSON)
    camera_config = db.Column(db.JSON)  # Full camera configuration from gphoto2
    last_config_update = db.Column(db.DateTime)  # When the camera config was last updated
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

class ScheduledSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    day_interval = db.Column(db.Integer, default=300)  # 5 minutes
    night_interval = db.Column(db.Integer, default=600)  # 10 minutes
    settings_day = db.Column(db.JSON)  # Camera settings for day
    settings_night = db.Column(db.JSON)  # Camera settings for night
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_run = db.Column(db.DateTime)
    next_run = db.Column(db.DateTime)