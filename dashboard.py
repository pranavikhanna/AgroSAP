import streamlit as st
import pandas as pd
from src.model import train_model
from src.simulate import run_simulation
from src.visualize import plot_results

st.title("AgroSAP: Soil Remediation Dashboard")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    model = train_model(data)
    results = run_simulation(data, model)
    st.write(results)
    plot_results(results)
