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

# Simple tag filter to help navigation
all_tags = sorted({tag for p in projects for tag in p.get("tags", [])})
selected_tags = st.multiselect("Filtrer par tags", options=all_tags, placeholder="Tous")

filtered = [
    p for p in projects
    if not selected_tags or any(tag in selected_tags for tag in p.get("tags", []))
]

if not filtered:
    st.info("Aucun projet ne correspond aux filtres.")
    st.stop()

for project in filtered:
    render_project_card(project)
