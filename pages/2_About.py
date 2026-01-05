import streamlit as st

st.set_page_config(page_title="About", page_icon="👋")

st.title("About")
st.write(
    "Je conçois et déploie des solutions Data/ML : feature stores, pipelines, API de scoring,"
    " dashboards Streamlit/BI, et monitoring de modèles."
)

st.subheader("Compétences clés")
st.markdown(
    """
    - Modélisation : classification, time series, RAG / NLP
    - MLOps : MLflow, CI/CD, conteneurisation, monitoring
    - Data : SQL, orchestration (Airflow), optimisation de pipelines
    - Front data apps : Streamlit, FastAPI + Streamlit hybrid
    """
)

st.subheader("Approche")
st.markdown(
    """
    - Itération rapide avec des POC mesurables
    - Obsédée par la lisibilité du code et l'automatisation des tests
    - Documentation concise et reproductibilité par défaut
    """
)
