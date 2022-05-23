class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value

