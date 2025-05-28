import json

def save_to_file(tasks, filename="tasks.json"):
    with open(filename, 'w') as f:
        json.dump(tasks, f)

def load_from_file(filename="tasks.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []