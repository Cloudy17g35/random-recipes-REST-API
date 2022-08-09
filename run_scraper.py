from random_recipes_api.scraper import Scraper
from random_recipes_api.s3_handler import S3Handler
from random_recipes_api.meal_types_mapper import mapper
import pandas as pd
from typing import Dict

bucket = 'przepisy2'
output_file_format = 'parquet'
s3_key_prefix = 'links_for_meal_type='


def write_dataframe_to_s3(
    bucket:str,
    key:str,
    data_frame:pd.DataFrame):
    s3_handler = S3Handler(bucket, key)
    s3_handler.write_parquet_file_from_dataframe(data_frame)
    print(f'dataframe with recipes is now saved on your s3 bucket: {bucket} with key:{key}')


def run_scraper():
    print('Scraping data started')
    meal_types_mapper:Dict[str, str] = mapper
    for meal_for_request, meal_type_in_english in meal_types_mapper.items():
        current_data:Dict[str, str] = Scraper().get_data_for_meal_type(meal_for_request)
        key:str = S3Handler.get_s3_key_name(s3_key_prefix, 
                                            meal_type_in_english, 
                                            output_file_format)
        df:pd.DataFrame = pd.DataFrame.from_dict(current_data)
        write_dataframe_to_s3(bucket, key, df)
    print('Scraping has been finished!')


if __name__ == '__main__':
    run_scraper()
    
