import streamlit as st

st.set_page_config(
    page_title="ML & Data Portfolio",
    page_icon="📊",
    layout="wide",
)

st.title("ML & Data Portfolio")
st.write(
    "Bienvenue sur mon portfolio. Explorez mes projets Machine Learning, mes expériences, et téléchargez mon CV."
)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(
        """
        ### Qui je suis
        Ingénieur Data/ML passionné par la mise en production de modèles, l'explicabilité,
        et les pipelines robustes. Je travaille aussi bien sur le prototypage rapide que
        sur l'industrialisation (MLOps, monitoring, CI/CD).

        ### Ce que vous trouverez ici
        - Une galerie de projets avec code source et démos live
        - Un CV téléchargeable
        - Quelques repères sur mon parcours
        """
    )

with col2:
    st.info(
        """
        💡 Astuce : utilisez la barre latérale Streamlit pour naviguer entre les pages
        (Projects, About, CV).
        """
    )

st.divider()
st.subheader("Focus rapide")

quick_cols = st.columns(3)
quick_cols[0].metric("Projets ML", "3+", "Production & expérimentation")
quick_cols[1].metric("Stacks", "PyData", "Streamlit, Airflow, MLflow")
quick_cols[2].metric("Ciblages", "MLOps", "Data Apps, RAG, Forecast")

st.caption("Prêt pour Streamlit Cloud : requirements.txt et multipage déjà configurés.")
