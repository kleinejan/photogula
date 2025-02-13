"""Mock camera settings data for testing and development"""

MOCK_CAMERA_SETTINGS = {
    "iso": {
        "name": "iso",
        "type": "RADIO",
        "current": "400",
        "choices": ["100", "200", "400", "800", "1600", "3200"]
    },
    "shutterspeed": {
        "name": "shutterspeed",
        "type": "MENU",
        "current": "1/125",
        "choices": ["30", "15", "8", "4", "2", "1", "1/2", "1/4", "1/8", "1/15", "1/30", "1/60", "1/125", "1/250", "1/500", "1/1000"]
    },
    "aperture": {
        "name": "aperture",
        "type": "RADIO",
        "current": "f/5.6",
        "choices": ["f/1.8", "f/2.0", "f/2.8", "f/4.0", "f/5.6", "f/8.0", "f/11", "f/16"]
    },
    "whitebalance": {
        "name": "whitebalance",
        "type": "RADIO",
        "current": "Auto",
        "choices": ["Auto", "Daylight", "Cloudy", "Tungsten", "Fluorescent", "Flash", "Custom"]
    },
    "focusmode": {
        "name": "focusmode",
        "type": "MENU",
        "current": "AF-S",
        "choices": ["AF-S", "AF-C", "MF"]
    },
    "imageformat": {
        "name": "imageformat",
        "type": "RADIO",
        "current": "RAW",
        "choices": ["RAW", "JPEG Fine", "JPEG Normal", "RAW+JPEG"]
    },
    "exposure_compensation": {
        "name": "exposure_compensation",
        "type": "RANGE",
        "current": "0",
        "range": {
            "min": "-3",
            "max": "+3",
            "step": "0.3"
        }
    }
}

def get_mock_settings():
    """Return mock camera settings"""
    return MOCK_CAMERA_SETTINGS
