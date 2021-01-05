
import os
import pandas as pd 
from PIL import Image, ImageDraw, ImageFont
from json_helper import JsonFileHelper


ROOT_OUTPUT_FOLDER = "output"
# --------------------------------------------
#          No changes beyond this point 
# --------------------------------------------

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

    def make_folders(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)        

    def clear_folder_contents(self, folder_name, file_extension = ".jpg"):
        for f in os.listdir(folder_name):
            if not f.endswith(file_extension):
                continue
            os.remove(os.path.join(folder_name, f))

    def write_text_on_image(self, name, dt):
        img = Image.open(self.config.background_image_file_location)
        width, height = img.size
        NAME_X = (width - (len(name)*55)) / 2 
        NAME_Y = 500
        DATE_X = (width - (len(dt)*40)) / 2 
        DATE_Y = 1422
        d1 = ImageDraw.Draw(img)
        name_Font = ImageFont.truetype(self.config.font_name, 150)
        date_Font = ImageFont.truetype(self.config.font_name, 100)
        d1.text((NAME_X, NAME_Y), name, font=name_Font, fill =(0, 0, 0))
        d1.text((DATE_X, DATE_Y), dt, font=date_Font, fill =(0, 0, 0))
        # img.show()
        file_name = name.lower().replace(" ", "-")
        output_file_path = os.path.join(ROOT_OUTPUT_FOLDER, config.output_folder_location, f"{self.config.output_file_prefix}[{dt}]-[{file_name}].jpg")
        img.save(output_file_path)
        return output_file_path

    def generate_certs(self):
        df = pd.read_csv(self.config.data_file_location)
        for index, row in df.iterrows():
            output_file_path = self.write_text_on_image(row['name'], row['date'])
            print("\t[" + row['name'] + "] certificate generated at: ", output_file_path)
        return df['name'].count()

    def get_config_json(config_file_path, config_schema_file_path):
        return config_json, config_schema_json

if __name__ == "__main__": 
    print("\n>>>>> START of Award Certificate Maker <<<<<\n");
    config_json = JsonFileHelper.GetJsonFromFile('config.json')
    config_schema_json = JsonFileHelper.GetJsonFromFile('config_schema.json')
    config = CertMakerConfig(config_json, config_schema_json)
    cert_maker = CertMaker(config)
    output_folder_name = os.path.join(ROOT_OUTPUT_FOLDER, config.output_folder_location)
    if os.path.exists(output_folder_name):
        print(f"Removing JPG files at folder [{output_folder_name}]..", end="")
        cert_maker.clear_folder_contents(output_folder_name)
    else:
        print(f"Creating output folder at[{output_folder_name}]..", end="")
        cert_maker.make_folders(output_folder_name)

    print("done!")
    print("Generating certificates ..");
    total_certs = cert_maker.generate_certs()
    print(f"done! Generated a total of {total_certs} certificates")

    print("\n>>>>> END of Award Certificate Maker <<<<<\n");

