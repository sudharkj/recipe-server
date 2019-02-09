# resources.py
import configparser
import os
import sys, traceback


class Config:
    """
    Load related configs.
    TODO make this singleton
    """
    PARENT_DIR = 'resources/'

    def __init__(self):
        dir = os.listdir(self.PARENT_DIR)
        files = [self.PARENT_DIR + file for file in dir if file.endswith('.ini')]
        self._app_config = configparser.ConfigParser()
        self._app_config.read(files)

        # update app_config with secrets
        secret_parser = configparser.ConfigParser()
        secret_parser.read(self._app_config.get('SECRET', 'keys-file-location'))
        for section in secret_parser.sections():
            try:
                self._app_config.add_section(section)
            except:
                traceback.print_exc(file=sys.stdout)
            for (key, value) in secret_parser.items(section):
                self._app_config.set(section, key, value)

    @property
    def app_config(self):
        return self._app_config
        