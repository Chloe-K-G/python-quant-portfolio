from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    df = df.copy()

    # Target: 1 if price goes up, 0 if down
    df['target'] = (df['returns'].shift(-1) > 0).astype(int)

    features = ['returns', 'ma50', 'ma200', 'volatility']
    X = df[features]
    y = df['target']

    model = RandomForestClassifier()
    model.fit(X, y)

    return model, X