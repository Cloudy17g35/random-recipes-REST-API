import pandas as pd
from random_recipes_api.s3_handler import S3Handler
from typing import Tuple


def get_sample(
        data_frame:pd.DataFrame,
        sample_size:int=1):
        return data_frame.sample(n=sample_size)


def get_dataframe(bucket_name:str, 
                  s3_key_prefix:str,
                  meal_type:str,
                  output_file_format:str) -> pd.DataFrame:
    s3_key = S3Handler.get_s3_key_name(s3_key_prefix, meal_type, output_file_format)
    s3_handler = S3Handler(bucket_name, key_name=s3_key)
    df = s3_handler.read_parquet_file_to_dataframe()
    return df


def get_random_recipe(
                bucket_name:str, 
                s3_key_prefix:str,
                meal_type:str,
                output_file_format:str) -> Tuple[str, str]:
        '''returns tuple with random recipe title and url'''

        df: pd.DataFrame = get_dataframe(bucket_name, 
                                         s3_key_prefix,
                                         meal_type,
                                         output_file_format)
        
        sample_from_dataframe:pd.DataFrame = get_sample(df)
        return sample_from_dataframe['title'].values[0], sample_from_dataframe['link'].values[0]