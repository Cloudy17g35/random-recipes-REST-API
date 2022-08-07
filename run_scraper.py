from random_recipes_api.scraper import Scraper
from random_recipes_api.s3_handler import S3Handler
import pandas as pd
from typing import Dict, List

bucket = 'przepisy-jadlonomia'
output_file_format = 'parquet'
s3_key_prefix = 'links_for_meal_type='


def write_dataframe_to_s3(
    bucket:str,
    key:str,
    data_frame:pd.DataFrame):
    s3_handler = S3Handler(bucket, key)
    s3_handler.write_parquet_file_from_dataframe(data_frame)
    print(f'dataframe with recipes is now saved on your s3 bucket: {bucket} with key:{key}')


def get_s3_key_name(meal_type:str):
    return f'{s3_key_prefix}{meal_type}.{output_file_format}'


def run_scraper():
    print('Scraping data started')
    meal_types:List[str] = ['sniadania',
                'przystawki', 'ciasta-i-desery',
                'do-chleba', 'zupy', 'napoje',
                'lunche-do-pracy', 'dania-glowne',
                'sosy-i-dodatki']
    for meal_type in meal_types:
        current_data:Dict[str, str] = Scraper().get_data_for_meal_type(meal_type)
        key:str = get_s3_key_name(meal_type)
        df:pd.DataFrame = pd.DataFrame.from_dict(current_data)
        write_dataframe_to_s3(bucket, key, df)


if __name__ == '__main__':
    run_scraper()
    
