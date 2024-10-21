import json
import sys

def parse_json(data):
    try:
        json_object = json.loads(data)
        if isinstance(json_object, dict):
            return "Valid JSON Object"
    except ValueError:
        pass
    return "Invalid JSON Object"

if __name__ == "__main__":
    input_data = input("Enter JSON data: ")
    result = parse_json(input_data)
    print(result)
    sys.exit(0 if result == "Valid JSON Object" else 1)