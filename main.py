
import os
import pandas as pd 
from PIL import Image, ImageDraw, ImageFont
from json_helper import JsonFileHelper


class CertMakerConfig:
    _jsonConfig = {}
    _schema_json_config = {}
    data_file_location = None
    background_image_file_location = None
    output_folder_location = None
    output_file_prefix = None
    font_name = None

    def __init__(self, json_config, schema_json_config):
        self._jsonConfig = json_config
        self.schema_json_config = schema_json_config
        self._parse_config_params(json_config, schema_json_config)

    def _parse_config_params(self, config, schema_json):
        is_valid_config, err = JsonFileHelper.ValidateJson(schema_json, config)

        if is_valid_config:
            self.data_file_location = config["DataFileLocation"]
            self.background_image_file_location = config["BackgroundImageFileLocation"]
            self.output_folder_location = config["OutputFolderLocation"]
            self.output_file_prefix = config["OutputFilePrefix"]
            self.font_name = config["FontName"]
        else:
            raise Exception(f"Config is either missing or invalid. \nErrorMessage:\n{err.message}")

class CertMaker:
    def __init__(self, config):
        if not config:
            raise("Need a valid config")

        self.config = config

    def clear_folder_contents(self, folder_name, file_extension = ".jpg"):
        for f in os.listdir(folder_name):
            if not f.endswith(file_extension):
                continue
            os.remove(os.path.join(folder_name, f))

    def write_text_on_image(self, name, dt):
        img = Image.open(self.config.background_image_file_location)
        d1 = ImageDraw.Draw(img)

        myFont = ImageFont.truetype(self.config.font_name, 7+86)
        name_x = 786-14-5-4-3-2-1
        name_y = 555-14-5-4-3-2-1
        dt_x = 786-14-5-4-3-2-1
        dt_y = 1555-140-5-4-3-2-1

        d1.text((name_x, name_y), name, font=myFont, fill =(0, 0, 0))
        d1.text((dt_x, dt_y), dt, font=myFont, fill =(0, 0, 0))
        # img.show()
        output_file_name = f"{self.config.output_file_prefix}{name}.jpg"
        img.save(f"{config.output_folder_location}/{output_file_name}")
        return output_file_name

    def generate_certs(self):
        df = pd.read_csv(self.config.data_file_location)
        for index, row in df.iterrows():
            output_file_path = self.write_text_on_image(row['name'].lower().replace(" ", "-"), row['date'])
            print("[" + row['name'] + "] cert generated at: ", output_file_path)

    def get_config_json(config_file_path, config_schema_file_path):
        return config_json, config_schema_json

if __name__ == "__main__": 
    print("\n\n>>>>> START OF Cert Maker <<<<<\n\n");
    config_json = JsonFileHelper.GetJsonFromFile('config.json')
    config_schema_json = JsonFileHelper.GetJsonFromFile('config_schema.json')
    config = CertMakerConfig(config_json, config_schema_json)
    cert_maker = CertMaker(config)
    print(f"removing files at folder [{config.output_folder_location}]");
    cert_maker.clear_folder_contents(config.output_folder_location)
    print("Generating certificates ..");
    cert_maker.generate_certs()

    print("\n\n>>>>> END OF Cert Maker <<<<<\n\n");

