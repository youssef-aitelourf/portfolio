# Portfolio ML / Data (Streamlit)

Application Streamlit multipage : Home, Projects, About, CV. Les projets sont déclarés dans `projects.json`; aucune modification UI n'est nécessaire pour en ajouter.

## Structure
- `streamlit_app.py` : page d'accueil
- `pages/1_Projects.py` : liste les projets à partir de `projects.json`
- `pages/2_About.py` : présentation
- `pages/3_CV.py` : téléchargement du CV (`cv.pdf` à la racine)
- `projects.json` : définition déclarative des projets (titre, description, tags, liens, images)
- `components/project_card.py` : composant réutilisable pour afficher un projet
- `utils/data_loader.py` : chargement + validation basique du JSON
- `.streamlit/config.toml` : thème
- `requirements.txt` : dépendances

## Ajouter un projet
1. Ouvrir `projects.json`
2. Ajouter un objet au tableau, avec les clés : `id`, `title`, `description`, `tags`, `github_url`, `demo_url`, `images` (liste d'URLs ou de chemins locaux)
3. Sauvegarder : la page Projects se mettra à jour automatiquement au prochain rafraîchissement

## Lancer en local
```bash
cd "$(dirname "$0")"
python -m streamlit run streamlit_app.py
```

## Déploiement Streamlit Cloud
- Pousser ce repo sur GitHub
- Dans Streamlit Cloud : "New app" → repo + branche → main file `streamlit_app.py`
- Les pages sont découvertes automatiquement via le dossier `pages/`
