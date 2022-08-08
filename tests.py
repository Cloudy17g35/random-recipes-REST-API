import pytest
from random_recipes_api.validators import MealTypeValidator
from random_recipes_api.s3_handler import S3Handler
import pandas as pd
bucket_name = 'przepisy-jadlonomia'


class TestValidator:
    
    def test_validator_valid_meal_type(self):
        valid_meal_type:str = 'Main_Courses'
        validated_data = MealTypeValidator.meal_type_must_be_valid(valid_meal_type)
        expected_result:str = 'main_courses'
        assert validated_data == expected_result
    
    def test_validator_valid_meal_type_with_whitespaces(self):
        valid_meal_type:str = '   Main_courses   '
        validated_data = MealTypeValidator.meal_type_must_be_valid(valid_meal_type)
        expected_result:str = 'main_courses'
        assert validated_data == expected_result
    
    def test_validator_invalid_meal_type(self):
        invalid_meal_type:str = 'foo'
        expected_result:ValueError = ValueError
        with pytest.raises(Exception) as e:
            MealTypeValidator.meal_type_must_be_valid(invalid_meal_type)
        assert e.type == expected_result
        


class TestS3Handler:
    
    def test_get_s3_key_name(self):
        s3_key_prefix = 'links_for_meal_type='
        meal_type = 'soups'
        output_file_format = 'parquet'
        actual  = S3Handler.get_s3_key_name(s3_key_prefix, meal_type, output_file_format)
        expected = 'links_for_meal_type=soups.parquet'
        assert actual == expected
    
    def test_read_parquet_file_to_dataframe(self):
        s3_key_prefix = 'links_for_meal_type='
        meal_type = 'soups'
        output_file_format = 'parquet'
        s3_key = S3Handler.get_s3_key_name(s3_key_prefix, meal_type, output_file_format)
        s3_handler = S3Handler(bucket_name='przepisy-jadlonomia', key_name=s3_key)
        df = s3_handler.read_parquet_file_to_dataframe()
        assert type(df) == pd.DataFrame