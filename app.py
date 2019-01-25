from flask import Flask
import json
import sys
import os
sys.path.insert(0, os.path.realpath('./'))
from api.app import api_bp, fetch_recipe_info

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello World!'
         
    app.register_blueprint(api_bp, url_prefix='/api')
    recipe_info = fetch_recipe_info('chicken')
    recipe = json.dumps(recipe_info) 
    print('I am here')
    print(type(recipe))
        
    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)
    