from pathlib import Path

import yaml


class Config:

    def __init__(self, path="config.yaml"):

        with open(path, "r") as file:

            self.config = yaml.safe_load(file)

    def get(self, key):

        return self.config[key]


config = Config()