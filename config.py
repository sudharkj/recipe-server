# resources.py
import configparser
import os


class Config:
    """
    Load related configs.
    TODO make this singleton
    """
    PARENT_DIR = 'resources/'

    def __init__(self):
        dir = os.listdir(self.PARENT_DIR)
        files = []
        for file in dir:
            files.append(self.PARENT_DIR + file)
        self._app_config = configparser.ConfigParser()
        self._app_config.read(files)

        # update app_config with secrets
        secret_parser = configparser.ConfigParser()
        secret_parser.read(self._app_config.get('SECRET', 'keys-file-location'))
        for section in secret_parser.sections():
            self._app_config.add_section(section)
            for (key, value) in  secret_parser.items(section):
                self._app_config.set(section, key, value)

    @property
    def app_config(self):
        return self._app_config
        