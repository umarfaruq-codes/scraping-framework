import pandas as pd


def save_csv(data, filepath : str):
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)