# apis/app.py
from flask import Blueprint
from flask_restful import Api

from apis.recipe_name import RecipeName as recipe_name
from apis.recipe_info import RecipeInfo as recipe_info


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# add urls to the blueprint
api.add_resource(recipe_name, '/recipe-name')

api.add_resource(recipe_info, '/recipe-info')

def __init__():
    None