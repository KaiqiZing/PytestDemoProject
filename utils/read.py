import configparser
import os
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")
class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path

    def read_data(self):
        f = open(self.data_path, encoding="utf8")
        data = yaml.safe_load(f)
        print(data['json_data'])
        return data

    def read_ini(self):  # 读取ini文件
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config


base_data = FileRead()
