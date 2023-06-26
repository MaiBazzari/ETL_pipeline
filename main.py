import os
# from dotenv import load_dotenv
# load_dotenv() # only for local testing
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_data
from src.load import df_to_s3


dbname=os.getenv('dbname')
host=os.getenv('host')
port=os.getenv('port')
user=os.getenv('user')
password=os.getenv('password')
aws_access_key_id=os.getenv('aws_access_key_id')
aws_secret_access_key_id=os.getenv('aws_secret_access_key_id')
key="bootcamp2/etl/mb_online_trans_cleaned.csv"
s3_bucket="waia-data-dump"


online_trans_clean =extract_transactional_data(dbname, host, port, user, password)
online_trans_dedup=identify_and_remove_duplicated_data(online_trans_clean)
df_to_s3(online_trans_dedup,key,s3_bucket,aws_access_key_id,aws_secret_access_key_id)






