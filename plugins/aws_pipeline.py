from utils.Load import upload_to_s3
import yaml

def load_config(config_path="config/config.yaml"):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def aws_pipeline(**kwargs):
    """Pulls file path from XCom."""
    try:
        ti = kwargs['ti']
        local_data_path = ti.xcom_pull(task_ids="reddit_extraction")

        if not local_data_path:
            raise FileNotFoundError("No file path found in XCom!")

        print(f"Received dataset path from XCom: {local_data_path}")

        config = load_config()

        aws_access_key_id = config['aws_access_key_id']
        aws_secret_access_key = config['aws_secret_access_key']
        aws_region = config['aws_region']
        aws_bucket_name = config['aws_bucket_name']

        upload_to_s3(local_data_path, "reddit-data/preprocessed_dataset.csv", 
                 aws_access_key_id, aws_secret_access_key, aws_region, aws_bucket_name)

    except Exception as e:
        raise e
