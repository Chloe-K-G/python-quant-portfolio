def generate_signals(model, X, df):
    df = df.copy()

    predictions = model.predict(X)
    df['signal'] = predictions

    # Convert 0 → -1 (sell)
    df['signal'] = df['signal'].replace(0, -1)

    return df


def backtest(df):
    df = df.copy()

    df['strategy_returns'] = df['returns'] * df['signal']
    df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()

    return df