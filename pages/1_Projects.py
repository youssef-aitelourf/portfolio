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

# Types principaux (pro / academic / personal)
TYPE_TAGS = {"pro", "academic", "personal"}
types_available = sorted({t for p in projects for t in p.get("tags", []) if t in TYPE_TAGS})
tech_tags = sorted({t for p in projects for t in p.get("tags", []) if t not in TYPE_TAGS})

col_type, col_tech = st.columns([1, 2])
with col_type:
    selected_type = st.selectbox(
        "Type de projet",
        options=["Tous"] + types_available,
        index=0,
    )
with col_tech:
    selected_tech = st.multiselect(
        "Technologies / Domaines",
        options=tech_tags,
        placeholder="Tous",
    )

col_flags = st.columns(2)
with col_flags[0]:
    require_github = st.checkbox("GitHub disponible")
with col_flags[1]:
    require_demo = st.checkbox("Démo disponible")


def match_project(p):
    tags = set(p.get("tags", []))
    if selected_type != "Tous" and selected_type not in tags:
        return False
    if selected_tech and not tags.intersection(selected_tech):
        return False
    if require_github and not p.get("github_url"):
        return False
    if require_demo and not p.get("demo_url"):
        return False
    return True


filtered = [p for p in projects if match_project(p)]

if not filtered:
    st.info("Aucun projet ne correspond aux filtres.")
    st.stop()

for project in filtered:
    render_project_card(project)
