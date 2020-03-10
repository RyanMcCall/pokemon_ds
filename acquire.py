import pandas as pd

def acquire_data():
    return pd.read_csv('pokemon.csv')