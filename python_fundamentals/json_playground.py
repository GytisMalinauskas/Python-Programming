import json

def main():
    data = {
        "message": ["1st item", "2nd item"],
        "temperature": 0.2
    }
    text = json.dump