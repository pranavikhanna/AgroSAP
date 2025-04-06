from flask import Flask, request, jsonify
from src.model import train_model
from src.simulate import run_simulation
import pandas as pd

app = Flask(__name__)

@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json
    df = pd.DataFrame(data)
    model = train_model(df)
    results = run_simulation(df, model)
    return results.to_json(orient="records")

if __name__ == "__main__":
    app.run(debug=True)
