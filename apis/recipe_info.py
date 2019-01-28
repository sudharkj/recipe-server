# apis/recipe_info.py
from flask import request, current_app
from flask_restful import Resource

from utils.helper import load_modules


class RecipeInfo(Resource):
    """
    Controller for api/recipe-info
    """
    EMPTY_ARGS = 'GET api/recipe-info has no request params'
    EMPTY_RECIPE_NAME_ARG = 'GET api/recipe-info has no recipe name in request params'

    def __init__(self):
        app_config = current_app.config['APP_CONFIG']

        recipe_module = load_modules(app_config.get('RECIPE_API', 'module-path'))
        self.get_recipe_info = recipe_module.get_recipe_info

        self.max_results = app_config.get('RECIPE_API', 'max-results')
        
        recipe_app_credentials = current_app.config['APP_CONFIG'].get('SECRET', 'keys-file-location')
        
        self.recipe_app_id = recipe_app_credentials['RECIPE_API_CONFIG']['RECIPE_APP_ID']
        self.recipe_app_key = recipe_app_credentials['RECIPE_API_CONFIG']['RECIPE_APP_KEY']
        print('Initialized api/recipe-info handlers')

    def get(self, recipe_name):
        """
        Returns the recipe information from the uri.
        : returns: Top results of the recipe information using the recipe name.
        """

        if request.args is None:
            raise ValueError(self.EMPTY_ARGS)
        if request.args['recipe_name'] is None or request.args['recipe_name'] == '':
            raise ValueError(self.EMPTY_RECIPE_NAME_ARG)

        return self.get_recipe_info(self.recipe_app_id, self.recipe_app_key, recipe_name, max_results=int(self.max_results))
