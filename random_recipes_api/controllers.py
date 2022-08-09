from random_recipes_api import pandas_dataframe
from random_recipes_api import validators
from pydantic import ValidationError
from random_recipes_api import responses

bucket_name = 'przepisy-jadlonomia'
s3_key_prefix = 'links_for_meal_type='
output_file_format = 'parquet'


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
    return {'recipe_title': recipe_title, 'recipe_url': recipe_url}



