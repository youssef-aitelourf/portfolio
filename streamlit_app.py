from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="ML & Data Portfolio",
    page_icon="📊",
    layout="wide",
)

# Contact + resources
NAME = "Youssef AIT ELOURF"
EMAIL = "youssef.aitelourf@gmail.com"
PHONE = "+1 (581) 672-2103"
LINKEDIN = "https://www.linkedin.com/in/youssef-ait-elourf-223316355/"
GITHUB = "https://github.com/youssef-aitelourf"
CV_PATH = Path(__file__).resolve().parent / "cv.pdf"


st.title("ML & Data Portfolio")

hero_left, hero_right = st.columns([1.6, 1])
with hero_left:
    st.markdown(
        f"""
        ### {NAME}
        Ingénieur Data/IA (ECE Paris) en double diplomation UQAR (Maîtrise IA/ML). Passionné par l'IA appliquée,
        les systèmes multi-agents, le NLP et l'IA générative. Recherche un stage à partir de mai 2026 (Montréal/Québec)
        en Machine Learning Engineer, Data Scientist ou Data Engineer.
        """
    )
    st.markdown(
        """
        - Mise en production de modèles (MLOps, monitoring, CI/CD)
        - Optimisation de pipelines et coûts cloud
        - Data apps et expériences utilisateurs via Streamlit/BI
        """
    )

    btn_cols = st.columns([1, 1, 1])
    with btn_cols[0]:
        if CV_PATH.exists():
            with CV_PATH.open("rb") as f:
                st.download_button(
                    "Telecharger le CV",
                    data=f.read(),
                    file_name="cv.pdf",
                    mime="application/pdf",
                    type="primary",
                )
        else:
            st.button("CV manquant", disabled=True)
    with btn_cols[1]:
        st.link_button("LinkedIn", LINKEDIN, type="secondary")
    with btn_cols[2]:
        st.link_button("GitHub", GITHUB, type="secondary")

with hero_right:
    st.info(
        """
        **Coordonnees**
        
        Email : youssef.aitelourf@gmail.com
        Tel : +1 (581) 672-2103
        
        **Localisation**
        Quebec / Montreal (mobilite Canada)
        
        **Focus 2026**
        Stage ML/DS/DE - IA generative, NLP, systèmes multi-agents.
        """
    )

st.divider()

st.subheader("Focus rapide")
quick_cols = st.columns(3)
quick_cols[0].metric("Projets ML", "3+", "Prod & POC")
quick_cols[1].metric("Stacks", "PyData", "Streamlit, Spark, MLflow")
quick_cols[2].metric("Certifs", "Azure", "AZ-900, DP-100")

st.subheader("Parcours en bref")
timeline_cols = st.columns(3)
with timeline_cols[0]:
    st.markdown(
        """
        **2025-2026**  
        Maitre en informatique (IA/ML)  
        UQAR, Quebec
        """
    )
with timeline_cols[1]:
    st.markdown(
        """
        **2022-2026**  
        Ingenieur Data/IA  
        ECE Paris
        """
    )
with timeline_cols[2]:
    st.markdown(
        """
        **Experiences**  
        ML Engineer @ Eddmon / Le Kompa  
        Reductions couts cloud (~15%), agents IA adoptés (+80%).
        """
    )

st.caption("Navigation : utilisez la barre laterale Streamlit pour Projects, About, CV.")
