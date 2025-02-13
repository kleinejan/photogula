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
    return render_template('capture.html', settings=camera_settings)

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

@app.route('/api/camera/toggle', methods=['POST'])
def toggle_capture():
    status = camera.toggle_capture()
    return jsonify({"status": status})

@app.route('/api/camera/settings', methods=['POST'])
def update_settings():
    settings = request.json
    result = camera.update_settings(settings)
    return jsonify(result)

with app.app_context():
    import models
    db.create_all()