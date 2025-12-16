# 📊 Projet ML SEA3 - Application d'Analyse et Prévisions

Application Flask complète pour l'analyse de données, tests statistiques et prévisions utilisant le machine learning.

## 🌟 Fonctionnalités

- **📤 Upload de Données**: Support CSV, XLSX, XLS
- **📊 Tests Statistiques**: Tests de stationnarité, normalité, et autres analyses
- **🔮 Prévisions ML**: Modèles de machine learning pour prévisions temporelles
- **📈 Visualisations**: Graphiques interactifs avec Plotly et Matplotlib
- **🗺️ Cartographie**: Visualisation géographique avec Folium
- **👤 Authentification**: Système de connexion sécurisé
- **📜 Historique**: Suivi des tests et analyses effectués
- **💹 Données Boursières**: Intégration avec Yahoo Finance

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation Locale

1. **Cloner le repository**
```bash
git clone <your-repo-url>
cd Projet-ML-SEA3
```

2. **Créer un environnement virtuel**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**

Créer un fichier `.env` à la racine du projet:
```env
# Configuration Flask
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Configuration Cache (optionnel)
CACHE_TYPE=SimpleCache

# APIs Boursières (optionnel)
ALPHAVANTAGE_KEY=your-alpha-vantage-key
IEX_CLOUD_API_KEY=your-iex-cloud-key

# Logging
LOG_LEVEL=INFO
```

5. **Lancer l'application**
```bash
python app.py
```

L'application sera accessible sur `http://localhost:5000`

## 🌐 Déploiement sur Vercel

### Configuration Vercel

1. **Installer Vercel CLI** (optionnel)
```bash
npm i -g vercel
```

2. **Variables d'environnement Vercel**

Dans votre dashboard Vercel, configurez:
- `SECRET_KEY`: Clé secrète Flask (générer avec `python -c "import secrets; print(secrets.token_hex(32))"`)
- `FLASK_ENV`: `production`
- Autres variables selon vos besoins (APIs, cache, etc.)

3. **Déployer**

Via Vercel CLI:
```bash
vercel
```

Ou via GitHub:
- Connectez votre repository à Vercel
- Vercel détectera automatiquement la configuration
- Le déploiement se fera automatiquement à chaque push

### Structure pour Vercel

```
Projet-ML-SEA3/
├── api/
│   └── index.py          # Point d'entrée Vercel
├── app/                  # Package Flask principal
├── vercel.json          # Configuration Vercel
├── requirements.txt     # Dépendances Python
└── README.md
```

## 📁 Structure du Projet

```
Projet-ML-SEA3/
├── api/                      # Vercel serverless functions
│   └── index.py
├── app/                      # Package Flask principal
│   ├── auth/                # Authentification
│   ├── blueprints/          # Modules de l'application
│   │   ├── home/
│   │   ├── upload/
│   │   ├── tests/
│   │   ├── previsions/
│   │   ├── visualisation/
│   │   └── cartographie/
│   ├── models/              # Modèles de données et ML
│   ├── services/            # Services (APIs, etc.)
│   ├── static/              # Fichiers statiques (CSS, JS)
│   ├── templates/           # Templates HTML
│   ├── __init__.py          # Factory de l'app
│   ├── config.py            # Configuration
│   └── utils.py             # Utilitaires
├── tests/                   # Tests unitaires
├── scripts/                 # Scripts utilitaires
├── app.py                   # Point d'entrée développement
├── wsgi.py                  # Point d'entrée production (Gunicorn)
├── requirements.txt         # Dépendances
└── vercel.json             # Configuration Vercel
```

## 🧪 Tests

Lancer les tests:
```bash
pytest
```

Avec couverture:
```bash
pytest --cov=app tests/
```

## 🔧 Configuration

### Modes de Configuration

- **Development**: Debug activé, cache simple
- **Production**: Debug désactivé, sécurité renforcée, cache Redis recommandé
- **Testing**: Configuration pour tests automatisés

### Cache

En développement: `SimpleCache` (en mémoire)
En production: `Redis` recommandé

Configuration Redis:
```env
CACHE_TYPE=Redis
CACHE_REDIS_URL=redis://:password@host:port/db
```

### Sécurité

En production, assurez-vous de:
- Définir `SECRET_KEY` unique et sécurisée
- Utiliser HTTPS
- Configurer les cookies sécurisés
- Limiter les tentatives de connexion

## 📊 Utilisation

1. **Upload de fichiers**: Téléchargez vos données (CSV, XLSX)
2. **Tests statistiques**: Sélectionnez et exécutez des tests
3. **Visualisation**: Explorez vos données graphiquement
4. **Prévisions**: Utilisez les modèles ML pour des prévisions
5. **Cartographie**: Visualisez vos données géographiquement

## 🛠️ Technologies

- **Backend**: Flask 2.2.5
- **Base de données**: SQLAlchemy, SQLite/PostgreSQL
- **ML**: scikit-learn, XGBoost, statsmodels
- **Visualisation**: Plotly, Matplotlib, Folium
- **Frontend**: HTML, CSS, JavaScript
- **Déploiement**: Vercel, Gunicorn

## 📝 Scripts Utiles

```bash
# Développement
python app.py

# Production avec Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# Tests
pytest

# Générer une clé secrète
python -c "import secrets; print(secrets.token_hex(32))"
```

## 🐛 Dépannage

### Problème: Module non trouvé
```bash
pip install -r requirements.txt
```

### Problème: Erreur de base de données
Vérifiez que les dossiers nécessaires existent:
```bash
mkdir -p uploads logs
```

### Problème: Port déjà utilisé
Changez le port dans `.env`:
```env
PORT=8000
```

## 📄 Licence

[Votre licence ici]

## 👥 Auteurs

- Sossou Melchisedek (orsinimelchisedek@gmail.com)

## 🤝 Contribution

Les contributions sont les bienvenues! N'hésitez pas à ouvrir une issue ou un pull request.

---

**Note**: Pour la production, n'oubliez pas de:
- Configurer les variables d'environnement
- Utiliser une base de données production (PostgreSQL)
- Configurer Redis pour le cache
- Activer HTTPS
- Configurer les sauvegardes