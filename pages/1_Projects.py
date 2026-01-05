import streamlit as st

from components.project_card import render_project_card
from utils.data_loader import load_projects


st.set_page_config(page_title="Projects", page_icon="🧠")
st.title("Projects")
st.caption("Les projets sont chargés automatiquement depuis projects.json.")

projects = load_projects()

if not projects:
    st.warning("Aucun projet trouvé. Ajoutez vos projets dans projects.json.")
    st.stop()

# Séparer les projets par catégorie
pro_projects = [p for p in projects if "pro" in p.get("tags", [])]
personal_projects = [p for p in projects if "academic" in p.get("tags", []) or "personal" in p.get("tags", [])]

# Créer les onglets
tab1, tab2 = st.tabs(["💼 Projets dans le cadre de stages", "🚀 Projets personnels"])

with tab1:
    if not pro_projects:
        st.info("Aucun projet professionnel pour le moment.")
    else:
        st.markdown(f"**{len(pro_projects)} projet(s) professionnel(s)**")
        st.markdown("---")
        for project in pro_projects:
            render_project_card(project)

with tab2:
    if not personal_projects:
        st.info("Aucun projet personnel pour le moment.")
    else:
        # Filtre pour les projets avec démo
        show_only_demo = st.checkbox("Afficher uniquement les projets avec démo", key="demo_filter")
        
        # Filtrer les projets selon le checkbox
        filtered_personal = personal_projects
        if show_only_demo:
            filtered_personal = [p for p in personal_projects if p.get("demo_url")]
        
        st.markdown(f"**{len(filtered_personal)} projet(s) personnel(s)**")
        st.markdown("---")
        
        if not filtered_personal:
            st.info("Aucun projet avec démo disponible.")
        else:
            for project in filtered_personal:
                render_project_card(project)
