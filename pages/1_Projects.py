import streamlit as st

from components.project_card import render_project_card
from utils.data_loader import load_projects
from utils.translations import get_text


st.set_page_config(page_title="Portfolio de projets", page_icon="🧠")

# Initialize language in session state
if "language" not in st.session_state:
    st.session_state.language = "en"

# Language selector in sidebar
with st.sidebar:
    st.markdown(get_text("language", "fr"))
    lang_cols = st.columns(2)
    with lang_cols[0]:
        if st.button("🇫🇷 FR", use_container_width=True, key="btn_fr_proj"):
            st.session_state.language = "fr"
    with lang_cols[1]:
        if st.button("🇬🇧 EN", use_container_width=True, key="btn_en_proj"):
            st.session_state.language = "en"

lang = st.session_state.language

st.title(get_text("projects", lang))
st.caption(get_text("projects_loaded", lang))

projects = load_projects()

if not projects:
    st.warning(get_text("no_projects", lang))
    st.stop()

# Séparer les projets par catégorie
pro_projects = [p for p in projects if "pro" in p.get("tags", [])]
personal_projects = [p for p in projects if "academic" in p.get("tags", []) or "personal" in p.get("tags", [])]

# Créer les onglets
tab1, tab2 = st.tabs([
    get_text("professional_experience", lang),
    get_text("portfolio", lang)
])

with tab1:
    if not pro_projects:
        st.info(get_text("no_professional", lang))
    else:
        # Trier les projets : ceux avec GitHub en premier
        pro_projects_sorted = sorted(pro_projects, key=lambda p: p.get("github_url") is None)
        
        st.markdown(f"**{len(pro_projects_sorted)} {get_text('professional_count', lang)}**")
        st.markdown("---")
        for project in pro_projects_sorted:
            render_project_card(project, lang)

with tab2:
    if not personal_projects:
        st.info(get_text("no_personal", lang))
    else:
        # Filtre pour les projets avec démo
        show_only_demo = st.checkbox(get_text("demo_filter", lang), key="demo_filter")
        
        # Filtrer les projets selon le checkbox
        filtered_personal = personal_projects
        if show_only_demo:
            filtered_personal = [p for p in personal_projects if p.get("demo_url")]
        
        # Trier les projets : ceux avec GitHub en premier
        filtered_personal_sorted = sorted(filtered_personal, key=lambda p: p.get("github_url") is None)
        
        st.markdown(f"**{len(filtered_personal_sorted)} {get_text('personal_count', lang)}**")
        st.markdown("---")
        
        if not filtered_personal_sorted:
            st.info(get_text("no_demo", lang))
        else:
            for project in filtered_personal_sorted:
                render_project_card(project, lang)
