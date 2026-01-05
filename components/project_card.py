from typing import List, Dict
import streamlit as st


def render_project_card(project: Dict):
    """Render a project card with title, description, tags, and action buttons."""
    with st.container(border=True):
        header_cols = st.columns([4, 1])
        with header_cols[0]:
            st.subheader(project.get("title", "Untitled"))
            st.caption(
                ", ".join(project.get("tags", [])) or "No tags provided"
            )
        with header_cols[1]:
            st.markdown(
                f"**ID**: `{project.get('id', 'n/a')}`",
                help="Stable identifier used in projects.json",
            )

        st.write(project.get("description", "No description provided."))

        button_cols = st.columns(2)
        with button_cols[0]:
            if project.get("github_url"):
                st.link_button("GitHub", project["github_url"], type="primary")
            else:
                st.button("GitHub", disabled=True, help="No GitHub URL provided")
        with button_cols[1]:
            if project.get("demo_url"):
                st.link_button("Live Demo", project["demo_url"], type="secondary")
            else:
                st.button("Live Demo", disabled=True, help="No live demo URL provided")

        images: List[str] = project.get("images", []) or []
        if images:
            st.markdown("**Gallery**")
            img_cols = st.columns(min(3, len(images)))
            for idx, image_url in enumerate(images):
                with img_cols[idx % len(img_cols)]:
                    st.image(image_url, width="stretch")
