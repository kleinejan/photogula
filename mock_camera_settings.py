"""Mock camera settings data for testing and development"""

MOCK_CAMERA_SETTINGS = {
    "/main/status/manufacturer": {
        "full_path": "/main/status/manufacturer",
        "section_path": "/main/status",
        "name": "manufacturer",
        "readable_name": "Camera Manufacturer",
        "type": "TEXT",
        "current": "Canon",
        "choices": [],
        "readonly": True,
        "description": "Camera manufacturer name"
    },
    "/main/status/cameramodel": {
        "full_path": "/main/status/cameramodel",
        "section_path": "/main/status",
        "name": "cameramodel",
        "readable_name": "Camera Model",
        "type": "TEXT",
        "current": "EOS 5D Mark IV",
        "choices": [],
        "readonly": True,
        "description": "Camera model name"
    },
    "/main/status/batterylevel": {
        "full_path": "/main/status/batterylevel",
        "section_path": "/main/status",
        "name": "batterylevel",
        "readable_name": "Battery Level",
        "type": "TEXT",
        "current": "100%",
        "choices": [],
        "readonly": True,
        "description": "Battery level in percent"
    },
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
    "/main/actions/viewfinder": {
        "full_path": "/main/actions/viewfinder",
        "section_path": "/main/actions",
        "name": "viewfinder",
        "readable_name": "Viewfinder",
        "type": "TOGGLE",
        "current": "2",
        "choices": ["0", "1"],
        "readonly": False,
        "description": "Enable or disable the viewfinder"
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
    "/main/settings/capture": {
        "full_path": "/main/settings/capture",
        "section_path": "/main/settings",
        "name": "capture",
        "readable_name": "Capture",
        "type": "TOGGLE",
        "current": "0",
        "choices": ["0", "1"],
        "readonly": False,
        "description": "Capture an image"
    },
    "/main/settings/recordingmedia": {
        "full_path": "/main/settings/recordingmedia",
        "section_path": "/main/settings",
        "name": "recordingmedia",
        "readable_name": "Recording Media",
        "type": "MENU",
        "current": "Card",
        "choices": ["Card", "Card + Card"],
        "readonly": False,
        "description": "Recording media settings"
    },
    "/main/capturesettings/exposurecompensation": {
        "full_path": "/main/capturesettings/exposurecompensation",
        "section_path": "/main/capturesettings",
        "name": "exposurecompensation",
        "readable_name": "Exposure Compensation",
        "type": "RANGE",
        "current": "0",
        "range": {"min": "-5", "max": "5", "step": "0.3"},
        "readonly": False,
        "description": "Exposure compensation in EV"
    },
    "/main/capturesettings/iso": {
        "full_path": "/main/capturesettings/iso",
        "section_path": "/main/capturesettings",
        "name": "iso",
        "readable_name": "ISO Speed",
        "type": "MENU",
        "current": "400",
        "choices": ["Auto", "100", "200", "400", "800", "1600", "3200", "6400", "12800", "25600", "51200", "102400"],
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
        "choices": ["Bulb", "30", "25", "20", "15", "13", "10", "8", "6", "5", "4", "3.2", "2.5", "2", "1.6", "1.3", "1", "0.8", "0.6", "0.5", "0.4", "0.3", "1/4", "1/5", "1/6", "1/8", "1/10", "1/13", "1/15", "1/20", "1/25", "1/30", "1/40", "1/50", "1/60", "1/80", "1/100", "1/125", "1/160", "1/200", "1/250", "1/320", "1/400", "1/500", "1/640", "1/800", "1/1000", "1/1250", "1/1600", "1/2000", "1/2500", "1/3200", "1/4000", "1/5000", "1/6400", "1/8000"],
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
        "choices": ["f/1.2", "f/1.4", "f/1.8", "f/2", "f/2.2", "f/2.5", "f/2.8", "f/3.2", "f/3.5", "f/4", "f/4.5", "f/5.0", "f/5.6", "f/6.3", "f/7.1", "f/8", "f/9", "f/10", "f/11", "f/13", "f/14", "f/16", "f/18", "f/20", "f/22"],
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
        "choices": ["One Shot", "AI Focus", "AI Servo", "Manual"],
        "readonly": False,
        "description": "Focus mode setting"
    },
    "/main/capturesettings/continuousaf": {
        "full_path": "/main/capturesettings/continuousaf",
        "section_path": "/main/capturesettings",
        "name": "continuousaf",
        "readable_name": "Continuous AF",
        "type": "MENU",
        "current": "Off",
        "choices": ["Off", "On"],
        "readonly": False,
        "description": "Continuous auto-focus setting"
    },
    "/main/capturesettings/aspectratio": {
        "full_path": "/main/capturesettings/aspectratio",
        "section_path": "/main/capturesettings",
        "name": "aspectratio",
        "readable_name": "Aspect Ratio",
        "type": "MENU",
        "current": "3:2",
        "choices": ["3:2", "4:3", "16:9", "1:1"],
        "readonly": False,
        "description": "Photo aspect ratio"
    },
    "/main/capturesettings/autoexposuremode": {
        "full_path": "/main/capturesettings/autoexposuremode",
        "section_path": "/main/capturesettings",
        "name": "autoexposuremode",
        "readable_name": "Auto Exposure Mode",
        "type": "MENU",
        "current": "P",
        "choices": ["P", "TV", "AV", "Manual", "Bulb", "A_DEP", "DEP", "Custom", "Lock", "Green", "Night Portrait", "Sports", "Portrait", "Landscape", "Closeup", "Flash Off"],
        "readonly": False,
        "description": "Auto exposure mode setting"
    },
    "/main/capturesettings/drivemode": {
        "full_path": "/main/capturesettings/drivemode",
        "section_path": "/main/capturesettings",
        "name": "drivemode",
        "readable_name": "Drive Mode",
        "type": "MENU",
        "current": "Single",
        "choices": ["Single", "Continuous Low", "Continuous High", "Timer 10 sec", "Timer 2 sec", "Timer Continuous"],
        "readonly": False,
        "description": "Drive mode setting"
    },
    "/main/capturesettings/picturestyle": {
        "full_path": "/main/capturesettings/picturestyle",
        "section_path": "/main/capturesettings",
        "name": "picturestyle",
        "readable_name": "Picture Style",
        "type": "MENU",
        "current": "Standard",
        "choices": ["Standard", "Portrait", "Landscape", "Neutral", "Faithful", "Monochrome", "User Def 1", "User Def 2", "User Def 3"],
        "readonly": False,
        "description": "Picture style setting"
    },
    "/main/capturesettings/whitebalance": {
        "full_path": "/main/capturesettings/whitebalance",
        "section_path": "/main/capturesettings",
        "name": "whitebalance",
        "readable_name": "White Balance",
        "type": "MENU",
        "current": "Auto",
        "choices": ["Auto", "Daylight", "Shadow", "Cloudy", "Tungsten", "Fluorescent", "Flash", "Manual", "Color Temperature"],
        "readonly": False,
        "description": "White balance setting"
    },
    "/main/imgsettings/imageformat": {
        "full_path": "/main/imgsettings/imageformat",
        "section_path": "/main/imgsettings",
        "name": "imageformat",
        "readable_name": "Image Format",
        "type": "MENU",
        "current": "RAW",
        "choices": ["Large Fine JPEG", "Large Normal JPEG", "Medium Fine JPEG", "Medium Normal JPEG", "Small Fine JPEG", "Small Normal JPEG", "Smaller JPEG", "Tiny JPEG", "RAW + Large Fine JPEG", "RAW"],
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
        "choices": ["Large", "Medium", "Small", "Tiny"],
        "readonly": False,
        "description": "Image size setting"
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
    }
}

def get_mock_settings():
    """Return mock camera settings"""
    return MOCK_CAMERA_SETTINGS