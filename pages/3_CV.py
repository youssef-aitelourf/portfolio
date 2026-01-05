from pathlib import Path

import streamlit as st

st.set_page_config(page_title="CV", page_icon="📄")

st.title("CV")

CV_PATH = Path(__file__).resolve().parent.parent / "cv.pdf"

if not CV_PATH.exists():
    st.error("Le fichier cv.pdf est introuvable dans le répertoire racine.")
    st.stop()

with CV_PATH.open("rb") as f:
    cv_bytes = f.read()

st.download_button(
    label="Télécharger le CV",
    data=cv_bytes,
    file_name="cv.pdf",
    mime="application/pdf",
    type="primary",
)

st.caption("Le CV est servi directement depuis le fichier cv.pdf présent à la racine du projet.")
