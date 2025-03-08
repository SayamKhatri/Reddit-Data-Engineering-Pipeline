import pandas as pd
import numpy as np
def transform_data(df):
    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
    df['over_18'] = np.where((df['over_18'] == True), True, False)
    df['author'] = df['author'].astype(str)

    edited_mode = df['edited'].mode()
    df['edited'] = np.where(df['edited'].isin([True, False]), df['edited'], edited_mode).astype(bool)
    df['num_comments'] = df['num_comments'].astype(int)
    df['score'] = df['score'].astype(int)
    df['title'] = df['title'].astype(str)

    return df




