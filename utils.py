import os
import psutil
from astral import LocationInfo
from astral.sun import sun
from datetime import datetime
import logging

def get_system_info():
    try:
        disk = psutil.disk_usage('/')
        return {
            'disk_total': format_size(disk.total),
            'disk_used': format_size(disk.used),
            'disk_free': format_size(disk.free),
            'disk_percent': disk.percent,
            'memory': psutil.virtual_memory().percent,
            'cpu': psutil.cpu_percent()
        }
    except Exception as e:
        logging.error(f"System info error: {str(e)}")
        return {}

def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024

def get_twilight_times(location):
    try:
        city = LocationInfo(location)
        s = sun(city.observer, date=datetime.now())
        return {
            'dawn': s['dawn'],
            'sunrise': s['sunrise'],
            'sunset': s['sunset'],
            'dusk': s['dusk']
        }
    except Exception as e:
        logging.error(f"Twilight calculation error: {str(e)}")
        return None

def get_captured_images(page, per_page=20):
    try:
        image_dir = "captured_images"  # Configure this path
        if not os.path.exists(image_dir):
            return []
        
        all_images = sorted(
            [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg'))],
            key=lambda x: os.path.getmtime(os.path.join(image_dir, x)),
            reverse=True
        )
        
        start = (page - 1) * per_page
        end = start + per_page
        return all_images[start:end]
    except Exception as e:
        logging.error(f"Image listing error: {str(e)}")
        return []
