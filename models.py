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
    date = db.Column(db.Date, nullable=False)
    settings_day = db.Column(db.JSON)
    settings_night = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)