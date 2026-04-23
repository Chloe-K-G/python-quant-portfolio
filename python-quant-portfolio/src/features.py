import pandas as pd

def create_features(df):
    df = df.copy()

    df['returns'] = df['Close'].pct_change()
    df['ma50'] = df['Close'].rolling(50).mean()
    df['ma200'] = df['Close'].rolling(200).mean()
    df['volatility'] = df['returns'].rolling(20).std()

    df = df.dropna()
    return df