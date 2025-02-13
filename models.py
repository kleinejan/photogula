from app import db
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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

class ScheduledSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    camera_settings_id = db.Column(db.Integer, db.ForeignKey('camera_settings.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)  # Daily start time
    end_time = db.Column(db.Time, nullable=False)    # Daily end time
    days_of_week = db.Column(db.String(7))  # e.g., "1111111" for all days, "1000001" for weekends
    interval_seconds = db.Column(db.Integer, default=300)  # Capture interval in seconds
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_run = db.Column(db.DateTime)
    next_run = db.Column(db.DateTime)

    # Relationship to CameraSettings
    camera_settings = db.relationship('CameraSettings', backref='schedules')
