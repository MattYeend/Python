import json

DATA_FILE = "library_data.json"

def load_library_data():
    """Load library data from a file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("\nNo existing library data found. Starting fresh.")
        return {"books": []}
    except json.JSONDecodeError:
        print("\nError reading library data file. Starting fresh.")
        return {"books": []}

def save_library_data(library):
    """Save library data to a file."""
    with open(DATA_FILE, "w") as file:
        json.dump(library, file, indent=4)
    print("\nLibrary data saved successfully!")
