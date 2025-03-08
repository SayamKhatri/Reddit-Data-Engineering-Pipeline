def extract_posts(instance, subreddit,time_filter, limit):
    try:
        reddit_instance = instance.subreddit(subreddit)
        posts = reddit_instance.top(time_filter=time_filter, limit=limit)
        print("Posts Extracted")

        extracted_posts = []

        for post in posts:
            extracted_posts.append({
                'id': post.id,
                'title' : post.title,
                'selftext' : post.selftext,
                'score' : post.score,
                'num_comments' : post.num_comments,
                'author': post.author,
                'created_utc' : post.created_utc,
                'url': post.url,
                'over_18': post.over_18,
                'edited' : post.edited,
                'spoiler' : post.spoiler,
                'stickied'  : post.stickied
            })
        
        return extracted_posts

    except Exception as e:
        raise e