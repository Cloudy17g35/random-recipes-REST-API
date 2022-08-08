from random_recipes_api.pandas_dataframe import get_random_recipe
import random_recipes_api.validators as validators
from pydantic import ValidationError
from fastapi import HTTPException

bucket_name = 'przepisy-jadlonomia'
s3_key_prefix = 'links_for_meal_type='
output_file_format = 'parquet'


def get_random_recipe(meal_type:str):
    try:
        meal_type = validators.MealTypeValidator(meal_type)
    except ValidationError as e:
        raise HTTPException(status_code=400, 
                            detail=e.errors())
    recipe_title, recipe_url = get_random_recipe(
                                       bucket_name,
                                       s3_key_prefix,
                                       meal_type,
                                       output_file_format)
    return {'recipe_title': recipe_title, 'recipe_url': recipe_url}



