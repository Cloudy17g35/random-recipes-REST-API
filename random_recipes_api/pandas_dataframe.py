import pandas as pd
from random_recipes_api.s3_handler import S3Handler


def get_sample(
        data_frame:pd.DataFrame,
        sample_size:int=1):
        return data_frame.sample(n=sample_size)


def get_dataframe(bucket_name:str, 
                  s3_key_prefix:str,
                  meal_type:str,
                  output_file_format:str):
    s3_key = S3Handler.get_s3_key_name(s3_key_prefix, meal_type, output_file_format)
    s3_handler = S3Handler(bucket_name, key_name=s3_key)
    df = s3_handler.read_parquet_file_to_dataframe()
    return df
