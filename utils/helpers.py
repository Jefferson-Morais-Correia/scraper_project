import pandas as pd


def save_to_csv(data: pd.DataFrame, filename: str):
    data.to_csv(filename, index=False)
