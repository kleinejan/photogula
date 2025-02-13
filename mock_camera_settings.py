"""Mock camera settings data for testing and development"""

MOCK_CAMERA_SETTINGS = {
    "/main/actions/syncdatetimeutc": {
        "full_path": "/main/actions/syncdatetimeutc",
        "section_path": "/main/actions",
        "name": "syncdatetimeutc",
        "readable_name": "Sync Date Time UTC",
        "type": "TEXT",
        "current": "",
        "choices": [],
        "readonly": False,
        "description": "Synchronize camera date and time with PC"
    },
    "/main/settings/capturetarget": {
        "full_path": "/main/settings/capturetarget",
        "section_path": "/main/settings",
        "name": "capturetarget",
        "readable_name": "Capture Target",
        "type": "MENU",
        "current": "Memory card",
        "choices": ["Internal RAM", "Memory card"],
        "readonly": False,
        "description": "Storage location for captured images"
    },
    "/main/capturesettings/iso": {
        "full_path": "/main/capturesettings/iso",
        "section_path": "/main/capturesettings",
        "name": "iso",
        "readable_name": "ISO Speed",
        "type": "MENU",
        "current": "400",
        "choices": ["100", "200", "400", "800", "1600", "3200", "6400"],
        "readonly": False,
        "description": "ISO speed setting"
    },
    "/main/capturesettings/shutterspeed": {
        "full_path": "/main/capturesettings/shutterspeed",
        "section_path": "/main/capturesettings",
        "name": "shutterspeed",
        "readable_name": "Shutter Speed",
        "type": "MENU",
        "current": "1/125",
        "choices": ["30", "15", "8", "4", "2", "1", "1/2", "1/4", "1/8", "1/15", "1/30", "1/60", "1/125", "1/250", "1/500", "1/1000", "1/2000", "1/4000"],
        "readonly": False,
        "description": "Shutter speed setting"
    },
    "/main/capturesettings/aperture": {
        "full_path": "/main/capturesettings/aperture",
        "section_path": "/main/capturesettings",
        "name": "aperture",
        "readable_name": "Aperture",
        "type": "MENU",
        "current": "f/5.6",
        "choices": ["f/1.8", "f/2.0", "f/2.8", "f/4.0", "f/5.6", "f/8.0", "f/11", "f/16", "f/22"],
        "readonly": False,
        "description": "Aperture setting"
    },
    "/main/capturesettings/focusmode": {
        "full_path": "/main/capturesettings/focusmode",
        "section_path": "/main/capturesettings",
        "name": "focusmode",
        "readable_name": "Focus Mode",
        "type": "MENU",
        "current": "AF-S",
        "choices": ["AF-S", "AF-C", "MF"],
        "readonly": False,
        "description": "Focus mode setting"
    },
    "/main/capturesettings/focusareawrap": {
        "full_path": "/main/capturesettings/focusareawrap",
        "section_path": "/main/capturesettings",
        "name": "focusareawrap",
        "readable_name": "Focus Area Wrap",
        "type": "MENU",
        "current": "No Wrap",
        "choices": ["Wrap", "No Wrap"],
        "readonly": False,
        "description": "Focus point wrap setting"
    },
    "/main/capturesettings/autofocusarea": {
        "full_path": "/main/capturesettings/autofocusarea",
        "section_path": "/main/capturesettings",
        "name": "autofocusarea",
        "readable_name": "Autofocus Area",
        "type": "MENU",
        "current": "Single Area",
        "choices": ["Single Area", "Dynamic Area", "Auto Area", "3D Tracking"],
        "readonly": False,
        "description": "Autofocus area mode setting"
    },
    "/main/imgsettings/imageformat": {
        "full_path": "/main/imgsettings/imageformat",
        "section_path": "/main/imgsettings",
        "name": "imageformat",
        "readable_name": "Image Format",
        "type": "MENU",
        "current": "RAW",
        "choices": ["RAW", "JPEG Basic", "JPEG Normal", "JPEG Fine", "RAW+JPEG Basic", "RAW+JPEG Normal", "RAW+JPEG Fine"],
        "readonly": False,
        "description": "Image format setting"
    },
    "/main/imgsettings/imagesize": {
        "full_path": "/main/imgsettings/imagesize",
        "section_path": "/main/imgsettings",
        "name": "imagesize",
        "readable_name": "Image Size",
        "type": "MENU",
        "current": "Large",
        "choices": ["Large", "Medium", "Small"],
        "readonly": False,
        "description": "Image size setting"
    }
}

def get_mock_settings():
    """Return mock camera settings"""
    return MOCK_CAMERA_SETTINGS