import boto3
import os
# AWS S3 credentials
aws_access_key_id = 'xxxxxxxxxxxxxxxxxxxx'
aws_secret_access_key = 'xxxxxxxxxxxxxxxxxxxxxxx'
aws_session_token = 'xxxxxxxxxxxxxxxxxxxxx'

# Bucket name and prefix (folder path)
bucket_name = 'cs-staging'
prefix = 'exported_data/'

# Local folder path
local_folder = 'cs-staging-s3/'

# Create a boto3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)

# List all objects in the bucket with the given prefix
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    
# Iterate through each object and download it
for obj in response['Contents']:
    # Extract the key (filename) of the object
    key = obj['Key']
    # Define the local file path to save the object
    local_file_path = os.path.join(os.getcwd(), local_folder, key.replace(prefix, ''))
    # Ensure the local folder exists, create if not
    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
    # Download the object
    s3.download_file(bucket_name, key, local_file_path)
    print(f"Downloaded: {key}")