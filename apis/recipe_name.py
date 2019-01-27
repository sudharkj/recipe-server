# apis/recipe_name.py
from flask import request, current_app
from flask_restful import Resource

from utils.helper import load_modules


class RecipeName(Resource):
    """
    Controller for api/recipe-name
    """
    EMPTY_ARGS = 'GET api/recipe-name has no request params'
    EMPTY_URI_ARG = 'GET api/recipe-name has no uri in request params'
    EMPTY_IMAGE_CONTENT = 'POST api/recipe-name has no request data'

    def __init__(self):
        app_config = current_app.config['APP_CONFIG']

        vision_module = load_modules(app_config.get('VISION_API', 'module-path'))
        self.get_best_guess = vision_module.get_best_guess

        self.max_results = app_config.get('VISION_API', 'max-results')

        print('Initialized api/recipe-name handlers')

    def get(self):
        """
        Returns best guess of recipe names from a public uri of an image.
        :return: recipe names
        """
        if request.args is None:
            raise ValueError(self.EMPTY_ARGS)
        if request.args['uri'] is None or request.args['uri'] == '':
            raise ValueError(self.EMPTY_URI_ARG)

        return self.get_best_guess(uri=request.args['uri'], max_results=int(self.max_results))

    def post(self):
        """
        Returns best guess of recipe names from image binary content
        :return: recipe names
        """
        if request.data is None or request.data == '':
            raise ValueError(self.EMPTY_IMAGE_CONTENT)

        return self.get_best_guess(content=request.data, max_results=int(self.max_results))
