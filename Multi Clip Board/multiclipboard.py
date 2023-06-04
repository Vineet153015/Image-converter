import sys
import clipboard
import json

SAVED_DATA ="clipboard.json"


def save_items(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_items(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return{}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter the Key : ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA,data)
        print("Data Saved")

    elif command == "load":
        key = input("Enter the Key you want to load: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to Clipboard")
        else:
            print("Key does not exist")
    elif command == "list":
        print(data)
    else:
        print("Unknown Command")
else:
    print("Please pass exactly one command")