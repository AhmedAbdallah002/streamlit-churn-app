import streamlit as st
import pandas as pd

def home_page():
    st.title("📊 Application de Prédiction de Churn")
    st.markdown("Bienvenue ! Voici un aperçu des clients et du churn.")
    st.metric("Clients totaux", "7 000")
    st.metric("Churn actuel", "26%")

def exploration_page():
    st.title("🔍 Exploration des Données")
    st.write("Visualisez et comprenez vos données clients ici.")
    sample = pd.DataFrame({
        "Age": [23, 45, 36],
        "Churn": ["Oui", "Non", "Oui"]
    })
    st.dataframe(sample)

def performance_page():
    st.title("📈 Performance du Modèle")
    st.write("Évaluez la qualité du modèle ici.")
    st.info("Courbes ROC et Matrice de confusion seront ajoutées en Phase 2.")

def prediction_page():
    st.title("🤖 Prédiction Client")
    st.write("Entrez les informations d’un client pour prédire le churn.")
    age = st.number_input("Âge", min_value=18, max_value=100, value=30)
    tenure = st.slider("Ancienneté (mois)", 1, 72, 12)
    st.button("Prédire")
    st.success("Résultat de prédiction ici (placeholder)")
