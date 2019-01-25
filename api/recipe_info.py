# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 08:55:00 2019

@author: DAMAN
"""

"""
Edamam API
"""
import requests
from flask_restful import Resource

class Edamam(Resource):
    """
	Fetches the recipe information from the recipe name.
	"""
    def __init__(self, recipe_appid = None, recipe_appkey = None, connect_url = None, search_query = None):
        self.recipe_appid = recipe_appid
        self.recipe_appkey = recipe_appkey
        self.connect_url = connect_url
        self.search_query = search_query
   
    def get(self):
        """
		:param info: recipe name
		:returns: dictionary of recipe information
		"""
        url = self.connect_url.format(self.search_query, self.recipe_appid, self.recipe_appkey)
        response_obj = requests.get(url)
        response_text = response_obj.json()['hits']
        
        recipe_columns = ['source', 'url', 'ingredientLines', 'cautions', 'healthLabels', 'calories', 'image']
        recipes = dict()
        
        for response in response_text:
            recipe = response['recipe']
            dish = recipe['label']
            recipes[dish] = dict()
        
            for recipe_col in recipe_columns:
                recipes[dish][recipe_col] = recipe[recipe_col]
        return recipes
    		