import json
from jsonschema import validate, exceptions


class JsonFileHelper:
    @staticmethod
    def ValidateJson(json_schema, json_data):
        try:
            validate(instance=json_data, schema=json_schema)
            return True, None
        except exceptions.ValidationError as err:
            return False, err

    @staticmethod
    def GetJsonFromFile(file_path):
        f = open(file_path, "r").read()
        return json.loads(f)
