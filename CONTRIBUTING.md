# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer à ce projet!

## 🚀 Démarrage

1. **Fork le repository**
2. **Cloner votre fork**
```bash
git clone https://github.com/votre-username/Projet-ML-SEA3.git
cd Projet-ML-SEA3
```

3. **Créer une branche**
```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

4. **Installer les dépendances de développement**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install pytest pytest-flask pytest-cov black flake8
```

## 📝 Standards de Code

### Style Python
- Suivre PEP 8
- Utiliser Black pour le formatage
- Maximum 100 caractères par ligne

```bash
# Formater le code
black app/ tests/

# Vérifier le style
flake8 app/ tests/
```

### Structure des Commits
```
type(scope): description courte

Description détaillée si nécessaire

Fixes #123
```

Types:
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation
- `style`: Formatage
- `refactor`: Refactorisation
- `test`: Tests
- `chore`: Maintenance

### Tests
- Écrire des tests pour toute nouvelle fonctionnalité
- Maintenir la couverture de code > 80%

```bash
# Lancer les tests
pytest

# Avec couverture
pytest --cov=app tests/

# Tests spécifiques
pytest tests/test_home.py
```

## 🔍 Processus de Review

1. **Créer une Pull Request**
   - Description claire des changements
   - Référencer les issues liées
   - Ajouter des captures d'écran si UI

2. **Checklist PR**
   - [ ] Tests passent
   - [ ] Code formaté (Black)
   - [ ] Documentation mise à jour
   - [ ] Pas de conflits
   - [ ] Couverture de tests maintenue

3. **Review**
   - Au moins une approbation requise
   - Répondre aux commentaires
   - Mettre à jour selon les retours

## 🐛 Signaler un Bug

Utiliser le template d'issue avec:
- Description du bug
- Étapes pour reproduire
- Comportement attendu vs actuel
- Environnement (OS, Python version)
- Logs/captures d'écran

## 💡 Proposer une Fonctionnalité

1. Vérifier qu'elle n'existe pas déjà
2. Créer une issue de discussion
3. Décrire le cas d'usage
4. Proposer une implémentation

## 📚 Documentation

- Documenter les nouvelles fonctionnalités
- Mettre à jour le README si nécessaire
- Ajouter des docstrings aux fonctions

## ✅ Checklist Finale

Avant de soumettre:
- [ ] Code testé localement
- [ ] Tests unitaires ajoutés
- [ ] Documentation mise à jour
- [ ] Code formaté (Black)
- [ ] Pas de warnings flake8
- [ ] Commit messages clairs
- [ ] Branch à jour avec main

## 🙏 Merci!

Votre contribution est appréciée! 🎉