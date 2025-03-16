from pathlib import Path
import json
import os


def get_settings():
    '''
    Returns the current settings.
    '''
    settings_json = Path(__file__).parent / "settings.json"
    try:
        with open(settings_json, "r") as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError:
        return {"rows": 6, "columns": 7}

def set_settings(changes):
    '''
    Updates the settings with the given changes.
    '''
    settings_json = Path(__file__).parent / "settings.json"
    settings = get_settings()
    settings.update(changes)
    with open(settings_json, "w") as f:
        json.dump(settings, f, indent=4)

def clear_screen():
    '''
    Clears the screen.
    '''
    
    os.system('cls' if os.name == 'nt' else 'clear')
