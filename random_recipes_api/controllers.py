from random_recipes_api import pandas_dataframe
from random_recipes_api import validators
from pydantic import ValidationError
from random_recipes_api import responses
from random_recipes_api import config_file
from typing import Dict, Any

CONFIG_DATA:Dict[str, Any] = config_file.get_data()
bucket_name:str = CONFIG_DATA['bucket_name']
output_file_format:str = CONFIG_DATA['output_file_format']
s3_key_prefix:str = CONFIG_DATA['s3_key_prefix']


def get_random_recipe(meal_type:str):
    try:
        meal_type = validators.MealTypeValidator(meal_type=meal_type).meal_type
    except ValidationError as e:
        responses.abort_bad_request(e.errors())
    recipe_title, recipe_url = pandas_dataframe.get_random_recipe(
                                       bucket_name,
                                       s3_key_prefix,
                                       meal_type,
                                       output_file_format)
    
    return responses.valid_response(recipe_title, recipe_url)



