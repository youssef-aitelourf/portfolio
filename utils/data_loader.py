import json
from pathlib import Path
from typing import List, Dict

import streamlit as st


PROJECTS_FILE = Path(__file__).resolve().parent.parent / "projects.json"


@st.cache_data(show_spinner=False)
def load_projects() -> List[Dict]:
    """Load project metadata from projects.json with basic validation."""
    if not PROJECTS_FILE.exists():
        return []

    try:
        with PROJECTS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        st.error("projects.json is malformed. Please fix the JSON format.")
        return []

    if not isinstance(data, list):
        st.error("projects.json must contain a list of projects.")
        return []

    normalized = []
    for item in data:
        if not isinstance(item, dict):
            continue
        normalized.append({
            "id": item.get("id", "unknown"),
            "title": item.get("title", "Untitled"),
            "description": item.get("description", ""),
            "tags": item.get("tags", []),
            "github_url": item.get("github_url"),
            "demo_url": item.get("demo_url"),
            "images": item.get("images", []),
        })

    return normalized
