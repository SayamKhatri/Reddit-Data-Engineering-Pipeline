import yaml
from utils.connection import connect_reddit
from utils.Extraction import extract_posts
from utils.transform import transform_data
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

    post_df = transform_data(post_df)






