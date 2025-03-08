import boto3

def upload_to_s3(local_file_path, s3_file_name, aws_access_key_id, aws_secret_access_key, aws_region, aws_bucket_name):
    """Uploads a file to an S3 bucket using provided credentials."""
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )

        s3_client.upload_file(local_file_path, aws_bucket_name, s3_file_name)
        print(f"Successfully uploaded {local_file_path} to s3://{aws_bucket_name}/{s3_file_name}")

    except Exception as e:
        print(f"Error uploading to S3: {e}")
        raise e
