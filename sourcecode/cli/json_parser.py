import json

import cli.io


class JsonParser:

    def __init__(self, json):
        self.json = json

    @classmethod
    def load_file(cls, file):
        json_dict = json.load(open(file, "r", encoding="utf-8"))
        return cls(json_dict)

    def get(self, key, possible_values=None, required=True):
        if required:
            return self.__get_required(key, possible_values)
        else:
            return self.__get_optional(key, possible_values)

    def get_object(self, key):
        obj = self.json[key]

        if not isinstance(obj, dict):
            raise SyntaxError

        return self.json[key]


    def __get_required(self, key, possible_values=None):
        if key in self.json:
            value = self.json[key]

            if possible_values is not None and value not in possible_values:
                print(cli.io.error_message(key, value))
                value = cli.io.request(key, possible_values)
        else:
            value = cli.io.request(key, possible_values)
        return value

    def __get_optional(self, key, possible_values=None):
        if key not in self.json:
            return None

        value = self.json[key]

        if possible_values is not None and value not in possible_values:
            print(cli.io.error_message(key, value))
            value = cli.io.request_optional(key, possible_values)

        return value


class JsonObject:

    def __init__(self, name=None, values=set(), objects=set(), required=True):
        self.name = name
        self.values = values
        self.objects = objects
        self.required = required


class JsonValue:

    def __init__(self, key, required=True):
        self.key = key
        self.required = required
