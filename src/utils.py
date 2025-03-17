from pathlib import Path
import json
import os


def get_settings():
    """Load game settings from a JSON file.

    Reads settings from a JSON file located in the same directory.
    If the file doesn't exist, returns default settings.

    Returns:
        dict: A dictionary containing game settings (rows, columns).
    """
    settings_json = Path(__file__).parent / "settings.json"
    try:
        with open(settings_json, "r") as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError:
        # Return default settings if file doesn't exist
        return {"rows": 6, "columns": 7}


def set_settings(changes):
    """Save updated game settings to a JSON file.

    Args:
        changes (dict): Dictionary containing setting keys and new values.
    """
    settings_json = Path(__file__).parent / "settings.json"
    # Get current settings and update with changes
    settings = get_settings()
    settings.update(changes)
    # Write updated settings to file
    with open(settings_json, "w") as f:
        json.dump(settings, f, indent=4)


def clear_screen():
    """Clear the console screen.

    Uses the appropriate system command based on the operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")
