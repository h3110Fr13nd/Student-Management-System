import pandas as pd

def print_df_from_dict(d, index='enrollment'):
    df = pd.DataFrame(d).T
    df.index.name = index
    print(df)