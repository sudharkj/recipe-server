# app.py
import os

from flask import Flask

from apis.app import api_bp
from config import Config as configuration

app = Flask(__name__)

# generate config and make it available through-out the application
config = configuration()
app.config.update(
    APP_CONFIG=config.app_config
)

# set google credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = app.config['APP_CONFIG'].get('SECRET', 'google-keys-file-location')


@app.route('/')
def hello_world():
    return 'Kill Me!'


# register api blueprint
app.register_blueprint(api_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run()
