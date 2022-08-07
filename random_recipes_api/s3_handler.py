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

    @property
    def get_path_to_s3(self):
        return f"s3://{self.bucket_name}/{self.key_name}"

    def write_parquet_file_from_dataframe(self, data_frame):
        path = self.get_path_to_s3
        wr.s3.to_parquet(data_frame, path)

    def read_parquet_file_to_dataframe(self) -> pd.DataFrame:
        path = self.get_path_to_s3
        return wr.s3.read_parquet(path)
