import matplotlib.pyplot as plt
import streamlit as st

def plot_results(data):
    plt.figure()
    plt.plot(data["metal"], data["predicted"], label="Predicted Absorption")
    plt.xlabel("Metal Level")
    plt.ylabel("Absorption")
    plt.legend()
    st.pyplot(plt)
