import configparser
from flask import Blueprint
from flask_restful import Api
from api.recipe_info import Edamam

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

def fetch_recipe_info(search_query):
    # Fetch the API information
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    
    RECIPE_APP_ID = (config['RECIPE_API_CONFIG']['RECIPE_APP_ID']).strip('"\'')
    RECIPE_APP_KEY = config['RECIPE_API_CONFIG']['RECIPE_APP_KEY']
    CONNECT_URL = (config['RECIPE_API_CONFIG']['RECIPE_CONNECT_URL']).strip('"\'')
    
    print(RECIPE_APP_ID)
    print(RECIPE_APP_KEY)
    print(CONNECT_URL)
    
    recipes = api.add_resource(Edamam, '/recipeinfo', resource_class_kwargs={'recipe_appid': RECIPE_APP_ID, 'recipe_appkey': RECIPE_APP_KEY, 'connect_url': CONNECT_URL, 'search_query': 'chicken'})
    return recipes

