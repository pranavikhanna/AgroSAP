from sklearn.linear_model import LinearRegression
import pandas as pd

def train_model(data):
    X = data[["metal"]]
    y = data["absorption"]
    model = LinearRegression()
    model.fit(X, y)
    return model
