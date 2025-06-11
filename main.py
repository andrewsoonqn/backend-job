import json


def get_data():
    # 'F' in "False" should be lowercase instead
    # return '{"tiam": "bibendum", "lacus": 23.5, "sellus": False}'
    return '{"tiam": "bibendum", "lacus": 23.5, "sellus": false}'


def main():
    data = json.loads(get_data())
    print(data)


if __name__ == "__main__":
    main()
