from typing import List, Dict
import streamlit as st


def render_project_card(project: Dict, lang: str = "fr"):
    """Render a project card with title, description, tags, and action buttons."""
    # Select language version of title and description
    title = project.get("title_en") if lang == "en" else project.get("title", "Untitled")
    description = project.get("description_en") if lang == "en" else project.get("description", "")
    
    with st.container(border=True):
        header_cols = st.columns([4, 1])
        with header_cols[0]:
            st.subheader(title)
            st.caption(
                ", ".join(project.get("tags", [])) or "No tags provided"
            )
        with header_cols[1]:
            st.markdown(
                f"**ID**: `{project.get('id', 'n/a')}`",
                help="Stable identifier used in projects.json",
            )

        st.write(description or "No description provided.")

        button_cols = st.columns(2)
        with button_cols[0]:
            if project.get("github_url"):
                st.link_button("GitHub", project["github_url"], type="primary")
            else:
                st.button(
                    "GitHub",
                    disabled=True,
                    help="No GitHub URL provided",
                    key=f"gh-missing-{project.get('id', '')}",
                )
        with button_cols[1]:
            if project.get("demo_url"):
                st.link_button("Live Demo", project["demo_url"], type="secondary")
            else:
                st.button(
                    "Live Demo",
                    disabled=True,
                    help="No live demo URL provided",
                    key=f"demo-missing-{project.get('id', '')}",
                )

        images: List[str] = project.get("images", []) or []
        if images:
            st.markdown("**Gallery**")
            img_cols = st.columns(min(3, len(images)))
            for idx, image_url in enumerate(images):
                with img_cols[idx % len(img_cols)]:
                    st.image(image_url, width="stretch")
