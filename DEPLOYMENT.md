# 🚀 Guide de Déploiement

Ce guide explique comment déployer l'application sur différentes plateformes.

## 📋 Prérequis

Avant de déployer, assurez-vous d'avoir:
- Un compte sur la plateforme de déploiement
- Les variables d'environnement configurées
- Une clé secrète sécurisée générée

### Générer une clé secrète

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## 🌐 Déploiement sur Vercel

### Méthode 1: Via GitHub (Recommandé)

1. **Pusher votre code sur GitHub**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Connecter à Vercel**
   - Allez sur [vercel.com](https://vercel.com)
   - Cliquez sur "New Project"
   - Importez votre repository GitHub
   - Vercel détectera automatiquement qu'il s'agit d'un projet Python

3. **Configurer les variables d'environnement**

Dans Vercel Dashboard → Settings → Environment Variables:

```
SECRET_KEY=<votre-clé-secrète-générée>
FLASK_ENV=production
CACHE_TYPE=SimpleCache
```

Variables optionnelles:
```
ALPHAVANTAGE_KEY=<votre-clé-api>
IEX_CLOUD_API_KEY=<votre-clé-api>
LOG_LEVEL=WARNING
```

4. **Déployer**
   - Cliquez sur "Deploy"
   - Vercel construira et déploiera automatiquement
   - Vous recevrez une URL de production

### Méthode 2: Via Vercel CLI

1. **Installer Vercel CLI**
```bash
npm i -g vercel
```

2. **Se connecter**
```bash
vercel login
```

3. **Déployer**
```bash
vercel
```

4. **Déployer en production**
```bash
vercel --prod
```

### Configuration Vercel

Le fichier `vercel.json` est déjà configuré:
```json
{
  "buildCommand": "pip install -r requirements.txt",
  "devCommand": "python app.py",
  "installCommand": "pip install -r requirements.txt"
}
```

### Point d'entrée Vercel

Le fichier `api/index.py` sert de point d'entrée serverless pour Vercel.

## 🐳 Déploiement avec Docker (Optionnel)

### Créer un Dockerfile

```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Créer les dossiers nécessaires
RUN mkdir -p uploads logs

# Exposer le port
EXPOSE 5000

# Variable d'environnement
ENV FLASK_ENV=production

# Commande de démarrage
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--timeout", "120", "wsgi:app"]
```

### Construire et lancer

```bash
# Construire l'image
docker build -t flask-ml-app .

# Lancer le conteneur
docker run -p 5000:5000 \
  -e SECRET_KEY=your-secret-key \
  -e FLASK_ENV=production \
  flask-ml-app
```

## ☁️ Déploiement sur Heroku

1. **Créer une application Heroku**
```bash
heroku create votre-app-name
```

2. **Configurer les variables d'environnement**
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set FLASK_ENV=production
```

3. **Déployer**
```bash
git push heroku main
```

Les fichiers `Procfile` et `runtime.txt` sont déjà configurés.

## 🔧 Déploiement sur VPS (Linux)

### 1. Préparer le serveur

```bash
# Mettre à jour le système
sudo apt update && sudo apt upgrade -y

# Installer Python et pip
sudo apt install python3.13 python3-pip python3-venv nginx -y

# Installer supervisor pour gérer le processus
sudo apt install supervisor -y
```

### 2. Configurer l'application

```bash
# Cloner le repository
cd /var/www
sudo git clone <your-repo-url> flask-ml-app
cd flask-ml-app

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
pip install gunicorn

# Créer le fichier .env
sudo nano .env
# Ajouter vos variables d'environnement
```

### 3. Configurer Supervisor

```bash
sudo nano /etc/supervisor/conf.d/flask-ml-app.conf
```

Contenu:
```ini
[program:flask-ml-app]
directory=/var/www/flask-ml-app
command=/var/www/flask-ml-app/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 --timeout 120 wsgi:app
user=www-data
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flask-ml-app/err.log
stdout_logfile=/var/log/flask-ml-app/out.log
```

```bash
# Créer le dossier de logs
sudo mkdir -p /var/log/flask-ml-app

# Recharger supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start flask-ml-app
```

### 4. Configurer Nginx

```bash
sudo nano /etc/nginx/sites-available/flask-ml-app
```

Contenu:
```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /var/www/flask-ml-app/app/static;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

```bash
# Activer le site
sudo ln -s /etc/nginx/sites-available/flask-ml-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 5. Configurer HTTPS avec Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d votre-domaine.com
```

## 🔍 Vérification du Déploiement

### Tests de base

```bash
# Tester localement
curl http://localhost:5000/

# Tester en production
curl https://votre-domaine.com/
```

### Vérifier les logs

**Vercel:**
- Dashboard → Deployments → Logs

**Heroku:**
```bash
heroku logs --tail
```

**VPS:**
```bash
sudo supervisorctl tail -f flask-ml-app
sudo tail -f /var/log/nginx/error.log
```

## 🛡️ Sécurité en Production

### Checklist de sécurité

- [ ] `SECRET_KEY` unique et sécurisée
- [ ] `DEBUG=False` en production
- [ ] HTTPS activé
- [ ] Cookies sécurisés configurés
- [ ] Rate limiting activé
- [ ] Variables d'environnement sécurisées
- [ ] Logs configurés
- [ ] Sauvegardes régulières
- [ ] Monitoring actif

### Variables d'environnement sensibles

Ne jamais commiter:
- `SECRET_KEY`
- Clés API
- Mots de passe de base de données
- Tokens d'authentification

Utiliser `.env` localement et les variables d'environnement de la plateforme en production.

## 📊 Monitoring

### Vercel
- Utiliser Vercel Analytics
- Configurer les alertes

### Sentry (Optionnel)
```bash
pip install sentry-sdk[flask]
```

Dans `app/__init__.py`:
```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
```

## 🔄 Mise à jour

### Vercel
```bash
git push origin main
# Déploiement automatique
```

### Heroku
```bash
git push heroku main
```

### VPS
```bash
cd /var/www/flask-ml-app
sudo git pull
source venv/bin/activate
pip install -r requirements.txt
sudo supervisorctl restart flask-ml-app
```

## ❓ Dépannage

### Erreur: Module not found
```bash
pip install -r requirements.txt
```

### Erreur: Permission denied
```bash
sudo chown -R www-data:www-data /var/www/flask-ml-app
```

### Erreur: Port already in use
```bash
# Trouver le processus
sudo lsof -i :5000
# Tuer le processus
sudo kill -9 <PID>
```

### Logs Vercel
- Vérifier dans Dashboard → Deployments → Function Logs
- Augmenter le timeout si nécessaire

---

Pour plus d'aide, consultez la documentation officielle de votre plateforme de déploiement.