import json
import os

FILE = "data/reminders.json"

def load_reminders():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)

def save_reminder(title, datetime_str):
    print("title and datetime",title,datetime_str )
    reminders = load_reminders()
 

    reminders.append({
        "title": title,
        "datetime": datetime_str,
        "completed": False
    })

    with open(FILE, "w") as f:
        json.dump(reminders, f, indent=4)

def get_reminders():
    return load_reminders()