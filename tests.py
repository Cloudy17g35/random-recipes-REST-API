import pytest
from pydantic import ValidationError
from random_recipes_api.validators import MealTypeValidator
from random_recipes_api import s3_handler
import random_recipes_api.pandas_dataframe as pandas_dataframe
from random_recipes_api import config_file
import pandas as pd
from typing import Dict, Any


CONFIG_DATA:Dict[str, Any] = config_file.get_data()
bucket_name:str = CONFIG_DATA['bucket_name']
output_file_format:str = CONFIG_DATA['output_file_format']
s3_key_prefix:str = CONFIG_DATA['s3_key_prefix']

class TestValidator:
    
    def test_validator_valid_meal_type(self):
        valid_meal_type:str = 'Main_Courses'
        validated_data = MealTypeValidator(meal_type=valid_meal_type).meal_type
        expected_result:str = 'main_courses'
        assert validated_data == expected_result
    
    def test_validator_valid_meal_type_with_whitespaces(self):
        valid_meal_type:str = '   Main_courses   '
        validated_data = MealTypeValidator(meal_type=valid_meal_type).meal_type
        expected_result:str = 'main_courses'
        assert validated_data == expected_result
    
    def test_validator_invalid_meal_type(self):
        invalid_meal_type:str = 'foo'
        expected_result:ValidationError = ValidationError 
        with pytest.raises(Exception) as e:
            MealTypeValidator(meal_type=invalid_meal_type)
        assert e.type == expected_result
        


class TestS3Handler:
    
    def test_get_s3_key_name(self):
        meal_type = 'soups'
        actual  = s3_handler.S3Handler.get_s3_key_name(s3_key_prefix, meal_type, output_file_format)
        expected = 'links_for_meal_type=soups.parquet'
        assert actual == expected
    
    def test_read_parquet_file_to_dataframe(self):
        meal_type = 'soups'
        s3_key = s3_handler.S3Handler.get_s3_key_name(s3_key_prefix, meal_type, 
                                                      output_file_format)
        handler = s3_handler.S3Handler(bucket_name=bucket_name, 
                                       key_name=s3_key)
        df = handler.read_parquet_file_to_dataframe()
        assert type(df) == pd.DataFrame
        

class TestPandasDataframe:
    
    def test_get_dataframe_type(self):
        meal_type = 'soups'
        df = pandas_dataframe.get_dataframe(bucket_name,
                                       s3_key_prefix,
                                       meal_type,
                                       output_file_format)
        assert type(df) == pd.DataFrame
    
    
    def test_get_sample(self):
        meal_type = 'soups'
        df = pandas_dataframe.get_dataframe(bucket_name,
                                       s3_key_prefix,
                                       meal_type,
                                       output_file_format)
        sample:pd.DataFrame = pandas_dataframe.get_sample(df)
        actual_number_of_rows:int = sample.shape[0]
        expected_number_of_rows:int = 1
        assert actual_number_of_rows == expected_number_of_rows
        
    def test_get_random_meal_and_link(self):
        meal_type = 'soups'
        recipe_title, recipe_url = pandas_dataframe.get_random_recipe(bucket_name,
                                       s3_key_prefix,
                                       meal_type,
                                       output_file_format)
        assert isinstance(recipe_title, str)
        assert isinstance(recipe_url, str)