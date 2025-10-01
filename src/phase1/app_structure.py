import streamlit as st

def setup_navigation():
    menu = ["Accueil", "Exploration", "Performance", "Prédiction"]
    return st.sidebar.radio("Navigation", menu)
