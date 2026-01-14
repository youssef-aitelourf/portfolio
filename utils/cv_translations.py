"""
Detailed CV section translations (Experience, Education, Skills, Languages)
"""

CV_TRANSLATIONS = {
    "fr": {
        # ==== Experience 1 ====
        "exp1_title": "Ingénieur en Machine Learning et Intelligence artificielle - Temps partiel",
        "exp1_company": "Eddmon et Le Kompa | Août 2025 - Nov. 2025 | À distance (Canada) - Entreprise basée à Paris, France",
        "exp1_bullets": [
            "Contribution active à la stratégie IA de l'entreprise (agents multi-domaines, NLP, IA générative).",
            "Optimisation et maintenance continue des modèles en production, réduisant les coûts cloud de **~15%**.",
            "Développement de nouveaux projets IA parallèlement à mes études, générant un gain estimé de **4 à 6h/semaine** pour les équipes métiers."
        ],
        
        # ==== Experience 2 ====
        "exp2_title": "Ingénieur en Machine Learning et Intelligence artificielle - Stagiaire",
        "exp2_company": "Eddmon | Avril 2025 - Août 2025 | Paris, France",
        "exp2_bullets": [
            "Développement et déploiement d'agents IA intégrés au CRM et aux outils métiers, avec un taux d'adoption **> 80%** par les équipes.",
            "Mise en production d'outils adoptés par les équipes RH, Sales et CSM, réduisant le temps de traitement de certaines tâches de plusieurs minutes à **quelques secondes**.",
            "**Projets réalisés** :\n    - Transcription et analyse d'appels (comptes-rendus instantanés, gain de **100%** de temps de saisie)\n    - Génération automatique de fiches clients (**3–5 min → quelques secondes**)\n    - Réponses SMS/mails (délai de réponse **divisé par 5**)\n    - Algorithme de matching pour demandes spécifiques (**1h → quelques secondes**)",
            "**Outils** : Python, Hugging Face, LangChain, SQL, Docker, Google Cloud Platform, DigitalOcean."
        ],
        
        # ==== Experience 3 ====
        "exp3_title": "Architecte réseaux et cybersécurité - Stagiaire",
        "exp3_company": "ACG Cybersecurity | Juin 2023 - Août 2023 | Paris, France",
        "exp3_bullets": [
            "Conception d'architectures réseaux sécurisées (segmentation, firewalls, VPN, IDS/IPS), contribuant à réduire le risque d'incident critique de **~20%**.",
            "Audit des infrastructures existantes et recommandations d'amélioration, mises en œuvre sur **3 projets clients**.",
            "**Outils** : Cisco Packet Tracer, Wireshark, Nessus, protocoles VPN/IPSec/SSL."
        ],
        
        # ==== Education 1 ====
        "edu1_title": "Maîtrise en informatique - IA et Machine Learning",
        "edu1_school": "Université du Québec à Rimouski (UQAR) | 2025 - 2026 | Rimouski, Canada",
        "edu1_h26_label": "Hiver 2026 (H26)",
        "edu1_h26": [
            "Traitement numérique des images – 8INF804",
            "Gestion de projets informatiques – 8INF847",
            "Métaheuristiques en optimisation – 8INF852",
            "Management des équipes de projet – MGP7130"
        ],
        "edu1_a25_label": "Automne 2025 (A25)",
        "edu1_a25": [
            "Structures de données avancées et leurs algorithmes – 8INF840",
            "Intelligence artificielle – 8INF846",
            "Génie logiciel – 8INF851",
            "Sécurité informatique – 8INF857",
            "Sujets spéciaux – 8INF950"
        ],
        
        # ==== Education 2 ====
        "edu2_title": "Diplôme d'ingénieur d'état - Data et Intelligence Artificielle",
        "edu2_school": "École centrale d'électronique de Paris (ECE Paris) | 2022 - 2026 | Paris, France",
        "edu2_program": "Programme Big Data & Analytics",
        "edu2_s8": "Semestre 8 (S8) – ING4 – Majeure Data & IA",
        "edu2_s8_management": "Management",
        "edu2_s8_management_items": ["Management des entreprises", "Management des systèmes d'information", "Management de la relation individuelle"],
        "edu2_s8_tech": "Technologie & Informatique",
        "edu2_s8_tech_items": ["Cloud Computing", "Data Integration", "Advanced Machine Learning", "Mathematics for Data Scientists", "Functional Programming", "NoSQL Databases"],
        "edu2_s6": "Semestre 6 (S6) – ING3",
        "edu2_s6_management": "Management",
        "edu2_s6_management_items": ["Analyse financière et économique", "Droit du travail"],
        "edu2_s6_tech": "Technologie & Informatique",
        "edu2_s6_tech_items": ["Programmation orientée objet Java", "Initiation aux réseaux", "Probabilités et statistiques", "Calcul embarqué et traitement numérique du signal", "MOOC Nanotechnologies"],
        "edu2_s7": "Semestre 7 (S7) – ING4 – Majeure Data & IA",
        "edu2_s7_management": "Management",
        "edu2_s7_management_items": ["Gestion budgétaire", "Management d'équipe"],
        "edu2_s7_tech": "Technologie & Informatique",
        "edu2_s7_tech_items": ["Bases de données avancées", "Systèmes d'exploitation", "Big Data Framework", "Introduction to Business Intelligence", "Data Visualisation", "Introduction to Machine Learning", "Data Science with Python"],
        "edu2_s5": "Semestre 5 (S5) – ING3",
        "edu2_s5_management": "Management",
        "edu2_s5_management_items": ["Bases de gestion", "Fundamentals of Business"],
        "edu2_s5_tech": "Technologie & Informatique",
        "edu2_s5_tech_items": ["Algorithmique et programmation structurée", "Bases de données", "Programmation Web", "Prototypage électronique"],
        
        # ==== Education 3 ====
        "edu3_title": "Classes préparatoires MPSI/PSI",
        "edu3_school": "Lycée Franklin D. Roosevelt | 2020 - 2022 | Reims, France",
        
        # ==== Skills ====
        "skills_languages": "Langages",
        "skills_languages_items": "Python, R, Java, SQL, Scala",
        "skills_ai_ml": "IA, LLMs & ML",
        "skills_ai_ml_items": "PyTorch, TensorFlow, Scikit-learn, Keras, LangChain, Hugging Face, Pandas, NumPy, XGBoost, Transformers, Vector Databases (Pinecone)",
        "skills_big_data": "Big Data",
        "skills_big_data_items": "Apache Spark, Hadoop, Koalas",
        "skills_databases": "Bases de données",
        "skills_databases_items": "MySQL, PostgreSQL, MongoDB, NoSQL",
        "skills_cloud_devops": "Cloud & DevOps",
        "skills_cloud_devops_items": "Azure (certifié), Amazon Web Services (AWS), Google Cloud Platform (GCP), DigitalOcean, Docker, Kubernetes, MLOps",
        
        # ==== Languages & Certifications ====
        "lang_spoken": "Langues",
        "lang_spoken_items": [
            "Français (langue maternelle et DALF C1)",
            "Anglais (C1, TOEIC 955)",
            "Arabe (langue maternelle)"
        ],
        "lang_certifications": "Certifications",
        "lang_certifications_items": [
            "Azure AZ-900",
            "Azure DP-100",
            "MOOC Gestion de projets",
            "Python Data Scientist"
        ],
    },
    
    "en": {
        # ==== Experience 1 ====
        "exp1_title": "Machine Learning and Artificial Intelligence Engineer - Part-time",
        "exp1_company": "Eddmon and Le Kompa | August 2025 - Nov. 2025 | Remote (Canada) - Company based in Paris, France",
        "exp1_bullets": [
            "Active contribution to the company's AI strategy (multi-domain agents, NLP, generative AI).",
            "Optimization and continuous maintenance of production models, reducing cloud costs by **~15%**.",
            "Development of new AI projects in parallel with my studies, generating an estimated gain of **4 to 6 hours/week** for business teams."
        ],
        
        # ==== Experience 2 ====
        "exp2_title": "Machine Learning and Artificial Intelligence Engineer - Internship",
        "exp2_company": "Eddmon | April 2025 - August 2025 | Paris, France",
        "exp2_bullets": [
            "Development and deployment of AI agents integrated into CRM and business tools, with an adoption rate **> 80%** by teams.",
            "Production deployment of tools adopted by HR, Sales and CSM teams, reducing processing time for certain tasks from several minutes to **a few seconds**.",
            "**Projects completed**:\n    - Call transcription and analysis (instant reports, **100%** time savings on data entry)\n    - Automatic generation of customer profiles (**3–5 min → a few seconds**)\n    - SMS/email responses (**response time divided by 5**)\n    - Matching algorithm for specific requests (**1h → a few seconds**)",
            "**Tools**: Python, Hugging Face, LangChain, SQL, Docker, Google Cloud Platform, DigitalOcean."
        ],
        
        # ==== Experience 3 ====
        "exp3_title": "Network Architect and Cybersecurity - Internship",
        "exp3_company": "ACG Cybersecurity | June 2023 - August 2023 | Paris, France",
        "exp3_bullets": [
            "Design of secure network architectures (segmentation, firewalls, VPN, IDS/IPS), contributing to reducing critical incident risk by **~20%**.",
            "Audit of existing infrastructures and improvement recommendations, implemented on **3 client projects**.",
            "**Tools**: Cisco Packet Tracer, Wireshark, Nessus, VPN/IPSec/SSL protocols."
        ],
        
        # ==== Education 1 ====
        "edu1_title": "Master's Degree in Computer Science - AI and Machine Learning",
        "edu1_school": "Université du Québec à Rimouski (UQAR) | 2025 - 2026 | Rimouski, Canada",
        "edu1_h26_label": "Winter 2026 (H26)",
        "edu1_h26": [
            "Digital Image Processing – 8INF804",
            "IT Project Management – 8INF847",
            "Metaheuristics in Optimization – 8INF852",
            "Project Team Management – MGP7130"
        ],
        "edu1_a25_label": "Fall 2025 (A25)",
        "edu1_a25": [
            "Advanced Data Structures and their Algorithms – 8INF840",
            "Artificial Intelligence – 8INF846",
            "Software Engineering – 8INF851",
            "Computer Security – 8INF857",
            "Special Topics – 8INF950"
        ],
        
        # ==== Education 2 ====
        "edu2_title": "State Engineer Diploma - Data and Artificial Intelligence",
        "edu2_school": "École Centrale d'Électronique de Paris (ECE Paris) | 2022 - 2026 | Paris, France",
        "edu2_program": "Big Data & Analytics Program",
        "edu2_s8": "Semester 8 (S8) – ING4 – Major Data & IA",
        "edu2_s8_management": "Management",
        "edu2_s8_management_items": ["Business Management", "Information Systems Management", "Individual Relationship Management"],
        "edu2_s8_tech": "Technology & IT",
        "edu2_s8_tech_items": ["Cloud Computing", "Data Integration", "Advanced Machine Learning", "Mathematics for Data Scientists", "Functional Programming", "NoSQL Databases"],
        "edu2_s6": "Semester 6 (S6) – ING3",
        "edu2_s6_management": "Management",
        "edu2_s6_management_items": ["Financial and Economic Analysis", "Labor Law"],
        "edu2_s6_tech": "Technology & IT",
        "edu2_s6_tech_items": ["Object-Oriented Java Programming", "Introduction to Networks", "Probability and Statistics", "Embedded Computing and Digital Signal Processing", "Nanotechnologies MOOC"],
        "edu2_s7": "Semester 7 (S7) – ING4 – Major Data & IA",
        "edu2_s7_management": "Management",
        "edu2_s7_management_items": ["Budget Management", "Team Management"],
        "edu2_s7_tech": "Technology & IT",
        "edu2_s7_tech_items": ["Advanced Databases", "Operating Systems", "Big Data Framework", "Introduction to Business Intelligence", "Data Visualization", "Introduction to Machine Learning", "Data Science with Python"],
        "edu2_s5": "Semester 5 (S5) – ING3",
        "edu2_s5_management": "Management",
        "edu2_s5_management_items": ["Fundamentals of Management", "Fundamentals of Business"],
        "edu2_s5_tech": "Technology & IT",
        "edu2_s5_tech_items": ["Algorithms and Structured Programming", "Databases", "Web Programming", "Electronic Prototyping"],
        
        # ==== Education 3 ====
        "edu3_title": "Preparatory Classes MPSI/PSI",
        "edu3_school": "Lycée Franklin D. Roosevelt | 2020 - 2022 | Reims, France",
        
        # ==== Skills ====
        "skills_languages": "Languages",
        "skills_languages_items": "Python, R, Java, SQL, Scala",
        "skills_ai_ml": "AI, LLMs & ML",
        "skills_ai_ml_items": "PyTorch, TensorFlow, Scikit-learn, Keras, LangChain, Hugging Face, Pandas, NumPy, XGBoost, Transformers, Vector Databases (Pinecone)",
        "skills_big_data": "Big Data",
        "skills_big_data_items": "Apache Spark, Hadoop, Koalas",
        "skills_databases": "Databases",
        "skills_databases_items": "MySQL, PostgreSQL, MongoDB, NoSQL",
        "skills_cloud_devops": "Cloud & DevOps",
        "skills_cloud_devops_items": "Azure (certified), Amazon Web Services (AWS), Google Cloud Platform (GCP), DigitalOcean, Docker, Kubernetes, MLOps",
        
        # ==== Languages & Certifications ====
        "lang_spoken": "Languages",
        "lang_spoken_items": [
            "French (native language and DALF C1)",
            "English (C1, TOEIC 955)",
            "Arabic (native language)"
        ],
        "lang_certifications": "Certifications",
        "lang_certifications_items": [
            "Azure AZ-900",
            "Azure DP-100",
            "Project Management MOOC",
            "Python Data Scientist"
        ],
    }
}

def get_cv_text(key: str, lang: str = "fr"):
    """Get translated CV text by key and language."""
    return CV_TRANSLATIONS.get(lang, CV_TRANSLATIONS["fr"]).get(key, key)
