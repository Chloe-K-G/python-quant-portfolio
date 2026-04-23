from src.data import get_data
from src.features import create_features
from src.model import train_model
from src.strategy import generate_signals, backtest

import matplotlib.pyplot as plt

# Step 1: Get data
data = get_data("AAPL")

# Step 2: Prepare dataframe
df = data.to_frame(name="Close")

# Step 3: Features
df = create_features(df)

# Step 4: Train model
model, X = train_model(df)

# Step 5: Signals
df = generate_signals(model, X, df)

# Step 6: Backtest
df = backtest(df)

# Step 7: Plot results
df['cumulative_returns'].plot(title="Strategy Performance")
plt.show()