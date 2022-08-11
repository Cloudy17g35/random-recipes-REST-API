import pytest
from pydantic import ValidationError
from random_recipes_api.validators import MealTypeValidator
from random_recipes_api import s3_handler
import random_recipes_api.pandas_dataframe as pandas_dataframe
from random_recipes_api import config_file
import pandas as pd
import requests
import json
from typing import Dict, Any


CONFIG_DATA:Dict[str, Any] = config_file.get_data()
bucket_name:str = CONFIG_DATA['bucket_name']
output_file_format:str = CONFIG_DATA['output_file_format']
s3_key_prefix:str = CONFIG_DATA['s3_key_prefix']
port:int = CONFIG_DATA['port']
host:str = CONFIG_DATA['host']
endpoint:str= '/recipes/random_recipe/'
address:str = f'http://{host}:{port}{endpoint}'

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
        

class TestAPI:
    
    def test_valid_response_status_code(self):
        meal_type = 'breakfasts'
        address = f'http://{host}:{port}{endpoint}'
        params:Dict[str, str] = {
            'meal_type': meal_type
            }
        resp:requests.Response = requests.get(address, 
                                              params=params)
        actual_status_code:int = resp.status_code
        expected_status_code:int = 200
        assert actual_status_code == expected_status_code

    def test_valid_response_content_type_is_dict(self):
        meal_type = 'breakfasts'
        params:Dict[str, str] = {
            'meal_type': meal_type
            }
        resp:requests.Response = requests.get(address, 
                                              params=params,
                                              )
        actual_content:Any = json.loads(resp.text)
        expected_type = dict
        assert isinstance(actual_content, expected_type)
        
    def test_valid_response_content_keys_in_dict(self):
        meal_type = 'breakfasts'
        params:Dict[str, str] = {
            'meal_type': meal_type
            }
        resp:requests.Response = requests.get(address, 
                                              params=params,
                                              )
        actual_content:dict = json.loads(resp.text)
        actual_content_keys:set = set(actual_content.keys())
        expected_keys:set = set(['recipe_title', 'recipe_url'])
        assert expected_keys - actual_content_keys == set()
        
    def test_bad_request_status_code(self):
        meal_type = 'foo'
        params:Dict[str, str] = {
            'meal_type': meal_type
            }
        resp:requests.Response = requests.get(address, 
                                              params=params,
                                              )
        actual_status_code:int = resp.status_code
        expected_status_code:int = 400
        assert actual_status_code == expected_status_code