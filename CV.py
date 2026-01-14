from pathlib import Path

import streamlit as st

from utils.translations import get_text
from utils.cv_translations import get_cv_text


st.set_page_config(
    page_title="Curriculum Vitae",
    page_icon="📊",
    layout="wide",
)

# Initialize language in session state
if "language" not in st.session_state:
    st.session_state.language = "en"

# Language selector in sidebar
with st.sidebar:
    st.markdown(get_text("language", "fr"))
    lang_cols = st.columns(2)
    with lang_cols[0]:
        if st.button("🇫🇷 FR", use_container_width=True, key="btn_fr_cv"):
            st.session_state.language = "fr"
    with lang_cols[1]:
        if st.button("🇬🇧 EN", use_container_width=True, key="btn_en_cv"):
            st.session_state.language = "en"

# Contact + resources
NAME = "Youssef AIT ELOURF"
EMAIL = "youssef.aitelourf@gmail.com"
PHONE = "+1 (581) 672-2103"
LINKEDIN = "https://www.linkedin.com/in/youssef-ait-elourf-223316355/"
GITHUB = "https://github.com/youssef-aitelourf"
CV_FR = Path(__file__).resolve().parent / "cv-fr.pdf"
CV_EN = Path(__file__).resolve().parent / "cv-en.pdf"

lang = st.session_state.language

# En-tête avec nom et coordonnées
st.title(NAME)
st.markdown(f"{EMAIL} | {PHONE} | [LinkedIn]({LINKEDIN})")

# Boutons d'actions
btn_cols = st.columns([1, 1, 1, 1, 4])

# Button 1: Download FR
with btn_cols[0]:
    if CV_FR.exists():
        with CV_FR.open("rb") as f:
            st.download_button(
                get_text("download_cv_fr", lang),
                data=f.read(),
                file_name="cv-fr.pdf",
                mime="application/pdf",
                type="primary",
            )
    else:
        st.button("CV FR missing", disabled=True)

# Button 2: Download EN
with btn_cols[1]:
    if CV_EN.exists():
        with CV_EN.open("rb") as f:
            st.download_button(
                get_text("download_cv_en", lang),
                data=f.read(),
                file_name="cv-en.pdf",
                mime="application/pdf",
                type="primary",
            )
    else:
        st.button("CV EN missing", disabled=True)

# LinkedIn
with btn_cols[2]:
    st.link_button(get_text("linkedin", lang), LINKEDIN, type="secondary")

# GitHub
with btn_cols[3]:
    st.link_button(get_text("github", lang), GITHUB, type="secondary")

st.divider()

# === PROFIL ===
st.header(get_text("profile", lang))
st.markdown(get_text("profile_text", lang))

st.divider()

# === ONGLETS CV ===
tab1, tab2, tab3, tab4 = st.tabs([
    get_text("experiences", lang),
    get_text("education", lang),
    get_text("skills", lang),
    get_text("languages_certifications", lang)
])

with tab1:
    # Experience 1
    st.subheader(get_cv_text("exp1_title", lang))
    st.caption(get_cv_text("exp1_company", lang))
    for bullet in get_cv_text("exp1_bullets", lang):
        st.markdown(f"- {bullet}")

    st.divider()

    # Experience 2
    st.subheader(get_cv_text("exp2_title", lang))
    st.caption(get_cv_text("exp2_company", lang))
    for bullet in get_cv_text("exp2_bullets", lang):
        st.markdown(f"- {bullet}")

    st.divider()

    # Experience 3
    st.subheader(get_cv_text("exp3_title", lang))
    st.caption(get_cv_text("exp3_company", lang))
    for bullet in get_cv_text("exp3_bullets", lang):
        st.markdown(f"- {bullet}")

with tab2:
    # Education 1
    st.subheader(get_cv_text("edu1_title", lang))
    st.caption(get_cv_text("edu1_school", lang))
    
    st.markdown(f"**{get_cv_text('edu1_h26_label', lang)}**")
    for course in get_cv_text("edu1_h26", lang):
        st.markdown(f"- {course}")
    
    st.markdown(f"**{get_cv_text('edu1_a25_label', lang)}**")
    for course in get_cv_text("edu1_a25", lang):
        st.markdown(f"- {course}")

    st.divider()

    # Education 2
    st.subheader(get_cv_text("edu2_title", lang))
    st.caption(get_cv_text("edu2_school", lang))
    st.markdown(f"[{get_cv_text('edu2_program', lang)}]")
    
    courses_col1, courses_col2 = st.columns(2)
    
    with courses_col1:
        st.markdown(f"**{get_cv_text('edu2_s8', lang)}**")
        st.markdown(f"*{get_cv_text('edu2_s8_management', lang)}*")
        for item in get_cv_text("edu2_s8_management_items", lang):
            st.markdown(f"- {item}")
        st.markdown(f"*{get_cv_text('edu2_s8_tech', lang)}*")
        for item in get_cv_text("edu2_s8_tech_items", lang):
            st.markdown(f"- {item}")
        
        st.markdown(f"**{get_cv_text('edu2_s6', lang)}**")
        st.markdown(f"*{get_cv_text('edu2_s6_management', lang)}*")
        for item in get_cv_text("edu2_s6_management_items", lang):
            st.markdown(f"- {item}")
        st.markdown(f"*{get_cv_text('edu2_s6_tech', lang)}*")
        for item in get_cv_text("edu2_s6_tech_items", lang):
            st.markdown(f"- {item}")

    with courses_col2:
        st.markdown(f"**{get_cv_text('edu2_s7', lang)}**")
        st.markdown(f"*{get_cv_text('edu2_s7_management', lang)}*")
        for item in get_cv_text("edu2_s7_management_items", lang):
            st.markdown(f"- {item}")
        st.markdown(f"*{get_cv_text('edu2_s7_tech', lang)}*")
        for item in get_cv_text("edu2_s7_tech_items", lang):
            st.markdown(f"- {item}")
        
        st.markdown(f"**{get_cv_text('edu2_s5', lang)}**")
        st.markdown(f"*{get_cv_text('edu2_s5_management', lang)}*")
        for item in get_cv_text("edu2_s5_management_items", lang):
            st.markdown(f"- {item}")
        st.markdown(f"*{get_cv_text('edu2_s5_tech', lang)}*")
        for item in get_cv_text("edu2_s5_tech_items", lang):
            st.markdown(f"- {item}")

    st.divider()

    # Education 3
    st.subheader(get_cv_text("edu3_title", lang))
    st.caption(get_cv_text("edu3_school", lang))

with tab3:
    comp_col1, comp_col2 = st.columns(2)
    with comp_col1:
        st.markdown(
            f"""
            **{get_cv_text('skills_languages', lang)}**  
            {get_cv_text('skills_languages_items', lang)}
            
            **{get_cv_text('skills_ai_ml', lang)}**  
            {get_cv_text('skills_ai_ml_items', lang)}
            
            **{get_cv_text('skills_big_data', lang)}**  
            {get_cv_text('skills_big_data_items', lang)}
            """
        )

    with comp_col2:
        st.markdown(
            f"""
            **{get_cv_text('skills_databases', lang)}**  
            {get_cv_text('skills_databases_items', lang)}
            
            **{get_cv_text('skills_cloud_devops', lang)}**  
            {get_cv_text('skills_cloud_devops_items', lang)}
            """
        )

with tab4:
    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        st.markdown(f"**{get_cv_text('lang_spoken', lang)}**")
        for language in get_cv_text("lang_spoken_items", lang):
            st.markdown(f"- {language}")

    with lang_col2:
        st.markdown(f"**{get_cv_text('lang_certifications', lang)}**")
        for cert in get_cv_text("lang_certifications_items", lang):
            st.markdown(f"- {cert}")

st.divider()
st.caption(get_text("sidebar_help", lang))
