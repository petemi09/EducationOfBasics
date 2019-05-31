import json

def main():
    y = {
        "First Name": "Mitchell",
        "Last Name": "Petellin",
        "Age": 22,
        "Married": False,
        "Pets": None,
        "Cars": None
    }

    print(json.dumps(y, indent=5))


main()