import pandas as pd

def run_simulation(data, model):
    data["predicted"] = model.predict(data[["metal"]])
    return data
