from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Curriculum Vitae",
    page_icon="📊",
    layout="wide",
)

# Contact + resources
NAME = "Youssef AIT ELOURF"
EMAIL = "youssef.aitelourf@gmail.com"
PHONE = "+1 (581) 672-2103"
LINKEDIN = "https://www.linkedin.com/in/youssef-ait-elourf-223316355/"
GITHUB = "https://github.com/youssef-aitelourf"
CV_PATH = Path(__file__).resolve().parent / "cv.pdf"


# En-tête avec nom et coordonnées
st.title(NAME)
st.markdown(f"{EMAIL} | {PHONE} | [LinkedIn]({LINKEDIN})")

# Boutons d'actions
btn_cols = st.columns([1, 1, 1, 6])
with btn_cols[0]:
    if CV_PATH.exists():
        with CV_PATH.open("rb") as f:
            st.download_button(
                "📄 Télécharger le CV",
                data=f.read(),
                file_name="cv.pdf",
                mime="application/pdf",
                type="primary",
            )
    else:
        st.button("CV manquant", disabled=True)
with btn_cols[1]:
    st.link_button("💼 LinkedIn", LINKEDIN, type="secondary")
with btn_cols[2]:
    st.link_button("💻 GitHub", GITHUB, type="secondary")

st.divider()

# === PROFIL ===
st.header("Profil")
st.markdown(
    """
    Étudiant en dernière année de cycle ingénieur Data & IA à l'ECE Paris et en double diplomation à l'UQAR 
    (Maîtrise en informatique IA et Machine Learning). Passionné par l'IA appliquée et les systèmes de données 
    à grande échelle. Recherche un **stage à partir de mai 2026 à Montréal/Québec** en tant que 
    **Machine Learning Engineer, Data Scientist ou Data Engineer**, avec un intérêt particulier pour les systèmes 
    multi-agents, le NLP et l'IA générative appliquée aux domaines industriel, santé et finance.
    """
)

st.divider()

# === ONGLETS CV ===
tab1, tab2, tab3, tab4 = st.tabs(["💼 Expériences", "🎓 Formation", "🛠️ Compétences", "🌍 Langues & Certifications"])

with tab1:
    st.subheader("Ingénieur en Machine Learning et Intelligence artificielle - Temps partiel")
    st.caption("Eddmon et Le Kompa | Août 2025 - Nov. 2025 | À distance (Canada) - Entreprise basée à Paris, France")
    st.markdown(
        """
        - Contribution active à la stratégie IA de l'entreprise (agents multi-domaines, NLP, IA générative).
        - Optimisation et maintenance continue des modèles en production, réduisant les coûts cloud de **~15%**.
        - Développement de nouveaux projets IA parallèlement à mes études, générant un gain estimé de **4 à 6h/semaine** pour les équipes métiers.
        """
    )

    st.subheader("Ingénieur en Machine Learning et Intelligence artificielle - Stagiaire")
    st.caption("Eddmon | Avril 2025 - Août 2025 | Paris, France")
    st.markdown(
        """
        - Développement et déploiement d'agents IA intégrés au CRM et aux outils métiers, avec un taux d'adoption **> 80%** par les équipes.
        - Mise en production d'outils adoptés par les équipes RH, Sales et CSM, réduisant le temps de traitement de certaines tâches de plusieurs minutes à **quelques secondes**.
        - **Projets réalisés** :
            - Transcription et analyse d'appels (comptes-rendus instantanés, gain de **100%** de temps de saisie)
            - Génération automatique de fiches clients (**3–5 min → quelques secondes**)
            - Réponses SMS/mails (délai de réponse **divisé par 5**)
            - Algorithme de matching pour demandes spécifiques (**1h → quelques secondes**)
        - **Outils** : Python, Hugging Face, LangChain, SQL, Docker, Google Cloud Platform, DigitalOcean.
        """
    )

    st.subheader("Architecte réseaux et cybersécurité - Stagiaire")
    st.caption("ACG Cybersecurity | Juin 2023 - Août 2023 | Paris, France")
    st.markdown(
        """
        - Conception d'architectures réseaux sécurisées (segmentation, firewalls, VPN, IDS/IPS), contribuant à réduire le risque d'incident critique de **~20%**.
        - Audit des infrastructures existantes et recommandations d'amélioration, mises en œuvre sur **3 projets clients**.
        - **Outils** : Cisco Packet Tracer, Wireshark, Nessus, protocoles VPN/IPSec/SSL.
        """
    )

with tab2:
    st.subheader("Maîtrise en informatique - IA et Machine Learning")
    st.caption("Université du Québec à Rimouski (UQAR) | 2025 - 2026 | Rimouski, Canada")
    
    st.markdown("**Hiver 2026 (H26)**")
    st.markdown(
        """
        - [Traitement numérique des images – 8INF804](https://www.uqar.ca/cours/traitement-numerique-des-images/)
        - [Gestion de projets informatiques – 8INF847](https://www.uqar.ca/cours/gestion-de-projets-informatiques/)
        - [Métaheuristiques en optimisation – 8INF852](https://www.uqar.ca/cours/metaheuristiques-en-optimisation/)
        - [Management des équipes de projet – MGP7130](https://www.uqar.ca/cours/management-des-equipes-de-projet/)
        """
    )
    
    st.markdown("**Automne 2025 (A25)**")
    st.markdown(
        """
        - [Structures de données avancées et leurs algorithmes – 8INF840](https://www.uqar.ca/cours/structures-de-donnees-avancees-et-leurs-algorithmes/)
        - [Intelligence artificielle – 8INF846](https://www.uqar.ca/cours/intelligence-artificielle/)
        - [Génie logiciel – 8INF851](https://www.uqar.ca/cours/genie-logiciel/)
        - [Sécurité informatique – 8INF857](https://www.uqar.ca/cours/securite-informatique/)
        - [Sujets spéciaux – 8INF950](https://www.uqar.ca/cours/sujets-speciaux/)
        """
    )
    
    st.subheader("Diplôme d'ingénieur d'état - Data et Intelligence Artificielle")
    st.caption("École centrale d'électronique de Paris (ECE Paris) | 2022 - 2026 | Paris, France")
    st.markdown("[Programme Big Data & Analytics](https://www.ece.fr/en/program/engineering-degree-bac4-big-data-analytics-major/)")
    
    courses_col1, courses_col2 = st.columns(2)
    
    with courses_col1:
        st.markdown("**Semestre 8 (S8) – ING4 – Majeure Data & IA**")
        st.markdown("*Management :* Management des entreprises, Management des systèmes d'information, Management de la relation individuelle")
        st.markdown("*Technologie & Informatique :* Cloud Computing, Data Integration, Advanced Machine Learning, Mathematics for Data Scientists, Functional Programming, NoSQL Databases")
        
        st.markdown("**Semestre 6 (S6) – ING3**")
        st.markdown("*Management :* Analyse financière et économique, Droit du travail")
        st.markdown("*Technologie & Informatique :* Programmation orientée objet Java, Initiation aux réseaux, Probabilités et statistiques, Calcul embarqué et traitement numérique du signal, MOOC Nanotechnologies")
    
    with courses_col2:
        st.markdown("**Semestre 7 (S7) – ING4 – Majeure Data & IA**")
        st.markdown("*Management :* Gestion budgétaire, Management d'équipe")
        st.markdown("*Technologie & Informatique :* Bases de données avancées, Systèmes d'exploitation, Big Data Framework, Introduction to Business Intelligence, Data Visualisation, Introduction to Machine Learning, Data Science with Python")
        
        st.markdown("**Semestre 5 (S5) – ING3**")
        st.markdown("*Management :* Bases de gestion / Fundamentals of Business")
        st.markdown("*Technologie & Informatique :* Algorithmique et programmation structurée, Bases de données, Programmation Web, Prototypage électronique")
    
    st.subheader("Classes préparatoires MPSI/PSI")
    st.caption("Lycée Franklin D. Roosevelt | 2020 - 2022 | Reims, France")

with tab3:
    comp_col1, comp_col2 = st.columns(2)
    with comp_col1:
        st.markdown(
            """
            **Langages**  
            Python, R, Java, SQL, Scala
            
            **IA, LLMs & ML**  
            PyTorch, TensorFlow, Scikit-learn, Keras, LangChain, Hugging Face, Pandas, NumPy, XGBoost, Transformers, Vector Databases (Pinecone)
            
            **Big Data**  
            Apache Spark, Hadoop, Koalas
            """
        )

    with comp_col2:
        st.markdown(
            """
            **Bases de données**  
            MySQL, PostgreSQL, MongoDB, NoSQL
            
            **Cloud & DevOps**  
            Azure (certifié), Amazon Web Services (AWS), Google Cloud Platform (GCP), DigitalOcean, Docker, Kubernetes, MLOps
            """
        )

with tab4:
    lang_col1, lang_col2 = st.columns(2)
    with lang_col1:
        st.markdown(
            """
            **Langues**
            - Français (langue maternelle et DALF C1)
            - Anglais (C1, TOEIC 955)
            - Arabe (langue maternelle)
            """
        )

    with lang_col2:
        st.markdown(
            """
            **Certifications**
            - Azure AZ-900
            - Azure DP-100
            - MOOC Gestion de projets
            - Python Data Scientist
            """
        )

st.divider()
st.caption("💡 Utilisez la barre latérale pour naviguer vers Projects, About, ou CV.")
