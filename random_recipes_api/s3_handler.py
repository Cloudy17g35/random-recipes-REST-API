import awswrangler as wr
import pandas as pd


class S3Handler:
    '''class which is responsible for interacting with
    AWS s3 bucket'''
    def __init__(self, 
                bucket_name:str, 
                key_name:str):
        self.bucket_name = bucket_name
        self.key_name = key_name

    @staticmethod
    def get_s3_key_name(s3_key_prefix:str,
                        meal_type:str, 
                        output_file_format:str):
        return f'{s3_key_prefix}{meal_type}.{output_file_format}'
    
    @property
    def s3_url(self):
        return f"s3://{self.bucket_name}/{self.key_name}"

    def write_parquet_file_from_dataframe(self, data_frame):
        path = self.s3_url
        wr.s3.to_parquet(data_frame, path)

    def read_parquet_file_to_dataframe(self) -> pd.DataFrame:
        path = self.s3_url
        return wr.s3.read_parquet(path)
