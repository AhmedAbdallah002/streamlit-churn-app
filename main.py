import streamlit as st
from src.phase1.app_structure import setup_navigation
from src.phase1.basic_pages import home_page, exploration_page, performance_page, prediction_page

def main():
    st.set_page_config(
        page_title="Churn Prediction App",
        page_icon="📊",
        layout="wide"
    )

    # Menu navigation
    page = setup_navigation()

    # Router vers les pages
    if page == "Accueil":
        home_page()
    elif page == "Exploration":
        exploration_page()
    elif page == "Performance":
        performance_page()
    elif page == "Prédiction":
        prediction_page()

if __name__ == "__main__":
    main()
