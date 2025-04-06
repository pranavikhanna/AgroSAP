from src.ingest import load_data
from src.model import train_model
from src.simulate import run_simulation
from src.visualize import plot_results
from supabase_helpers import store_results

if __name__ == "__main__":
    data = load_data("data/soil_sample.csv")
    model = train_model(data)
    results = run_simulation(data, model)
    store_results(results)
    plot_results(results)

---
