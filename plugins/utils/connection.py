import praw 

def connect_reddit(client_id, secret, user_agent):
    try:
        reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret,
        user_agent=user_agent
        )
        print("Connection successfull")

        return reddit

    except Exception as e: 
        raise e 




