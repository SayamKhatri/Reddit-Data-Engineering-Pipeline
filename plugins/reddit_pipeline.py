import yaml
from utils.connection import connect_reddit
from utils.Extraction import extract_posts
from utils.transform import transform_data
from utils.Load import upload_to_s3
import pandas as pd
import os

def load_config(config_path="config/config.yaml"):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def reddit_pipeline(file_name, subreddit, time_filter, limit):

    # Connect to reddit
    config = load_config()
    client_id = config["client_id"]
    secret = config["reddit_secret_key"]


    instance = connect_reddit(client_id, secret, 'Agent')


    # Extract
    posts = extract_posts(instance, subreddit,time_filter, limit)
    post_df = pd.DataFrame(posts)

    # Transform
    post_df = transform_data(post_df)

    local_data_path = os.path.abspath(os.path.join(os.getcwd(), "data", "preprocessed_dataset.csv"))
    os.makedirs(os.path.dirname(local_data_path), exist_ok=True)
    post_df.to_csv(local_data_path, index=False)

    return local_data_path








