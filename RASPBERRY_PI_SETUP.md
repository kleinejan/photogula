# Raspberry Pi Setup Guide

## 1. System Requirements
First, update your Raspberry Pi:
```bash
sudo apt-get update
sudo apt-get upgrade
```

Install required system dependencies:
```bash
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib gphoto2
```

## 2. Python Packages
Install the required Python packages:
```bash
pip3 install flask flask-sqlalchemy psycopg2-binary gphoto2 gunicorn psutil flask-login oauthlib astral flask-wtf email-validator
```

## 3. Database Setup
Setup PostgreSQL database:
```bash
sudo -u postgres psql

# In the PostgreSQL prompt:
CREATE DATABASE timelapse;
CREATE USER pi WITH PASSWORD 'your_password_here';
GRANT ALL PRIVILEGES ON DATABASE timelapse TO pi;
\q
```

## 4. Environment Variables
Create a `.env` file in your project directory:
```bash
# Database connection
export DATABASE_URL="postgresql://pi:your_password_here@localhost/timelapse"

# Flask configuration
export FLASK_SECRET_KEY="your_secret_key_here"
```

Load the environment variables:
```bash
source .env
```

## 5. Running the Application
1. Clone or copy your project files to the Raspberry Pi
2. Navigate to your project directory
3. Run the application:
```bash
python3 main.py
```

The application will be available at `http://your_raspberry_pi_ip:5000`

## Important Notes:
1. Replace `your_password_here` with a secure password
2. Replace `your_secret_key_here` with a random string for security
3. Make sure your camera is connected and recognized by gphoto2
4. Test camera detection: `gphoto2 --auto-detect`
5. For autostart on boot, consider creating a systemd service

## Troubleshooting:
1. Camera not detected:
   ```bash
   sudo gphoto2 --auto-detect
   ```
2. Database connection issues:
   ```bash
   sudo systemctl status postgresql
   ```
3. Permission issues:
   ```bash
   sudo usermod -a -G plugdev $USER
   ```
