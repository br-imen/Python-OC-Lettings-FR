## OC-Lettings-Site

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Intégration de Sentry

Ce projet est configuré pour utiliser [Sentry](https://sentry.io/) pour le suivi des erreurs et la surveillance des performances. Sentry permet de capturer et de signaler les erreurs en temps réel, ce qui facilite l'identification et la correction des problèmes en production.

#### Configuration de Sentry

Pour configurer Sentry dans ce projet :

1. **Créer un compte Sentry** :
   - Si vous n'avez pas de compte Sentry, inscrivez-vous sur [sentry.io](https://sentry.io/signup/).
   - Créez un nouveau projet dans votre tableau de bord Sentry et sélectionnez "Django" comme plateforme.

2. **Installer le SDK Sentry** :
   - Le SDK Sentry est déjà inclus dans le fichier `requirements.txt`. Si vous devez l'ajouter manuellement, vous pouvez le faire avec la commande suivante :
     ```bash
     pip install sentry-sdk
     ```

3. **Configurer Sentry dans Django** :
   - Sentry est configuré dans le fichier `settings.py` de votre projet Django. La configuration essentielle ressemble à ceci :
     ```python
     import sentry_sdk
     from sentry_sdk.integrations.django import DjangoIntegration

     sentry_sdk.init(
         dsn="VOTRE_SENTRY_DSN",  # Remplacez par votre DSN Sentry
         integrations=[DjangoIntegration()],
         traces_sample_rate=1.0,  # Ajustez cette valeur selon vos besoins
         send_default_pii=True  # Cela permet d'envoyer des informations personnellement identifiables
     )
     ```

   - Remplacez `VOTRE_SENTRY_DSN` par le DSN (Data Source Name) fourni par Sentry pour votre projet.

4. **Configuration spécifique à l'environnement** :
   - Il est recommandé d'activer Sentry uniquement dans votre environnement de production. Vous pouvez configurer Sentry en fonction de l'environnement de cette manière :
     ```python
     import os

     if os.getenv('ENVIRONMENT') == 'production':
         sentry_sdk.init(
             dsn=os.getenv('SENTRY_DSN'),
             integrations=[DjangoIntegration()],
             traces_sample_rate=1.0,
             send_default_pii=True
         )
     ```

   - Assurez-vous que la variable d'environnement `SENTRY_DSN` est définie dans votre environnement de production.

5. **Gestion des erreurs personnalisée** :
   - Sentry peut également être utilisé pour capturer des erreurs ou des avertissements spécifiques dans votre application. Par exemple, vous pouvez capturer une exception manuellement :
     ```python
     import sentry_sdk

     try:
         # Du code qui pourrait lever une exception
         ...
     except Exception as e:
         sentry_sdk.capture_exception(e)
     ```


#### Vérification de l'intégration

Après la configuration, vous pouvez vérifier que Sentry capture correctement les erreurs :

1. Provoquez une erreur dans votre application (par exemple, une division par zéro délibérée) et vérifiez si elle apparaît dans votre tableau de bord Sentry.
2. Surveillez le tableau de bord Sentry pour vous assurer que les erreurs et les données de performances sont bien signalées.

### Déploiement

#### Récapitulatif

Le processus de déploiement est automatisé via une pipeline CI/CD configurée dans GitHub Actions. Lorsque des modifications sont poussées ou lorsqu'une pull request est fusionnée dans la branche `master`, la pipeline exécute des tests, construit une image Docker, et déploie automatiquement l'application sur un service d'hébergement Render. Cette approche assure une livraison continue, minimisant ainsi les risques d'erreurs manuelles et garantissant que la version la plus récente et stable de l'application est toujours en production.

#### Configuration Requise

Pour que le déploiement fonctionne correctement, les éléments suivants doivent être configurés :

1. **Secrets GitHub** : Les secrets suivants doivent être définis dans les paramètres du dépôt GitHub :
   - `SECRET_KEY` : Clé secrète utilisée par l'application pour diverses opérations sécurisées.
   - `DOCKER_HUB_USERNAME` et `DOCKER_HUB_PASSWORD` : Identifiants pour se connecter à Docker Hub.
   - `RENDER_DEPLOY_HOOK_URL` : URL du webhook de déploiement fourni par Render ou un autre service d'hébergement.

2. **Docker Hub** : Un compte Docker Hub configuré pour stocker l'image Docker de l'application.

3. **Service d'hébergement (ex. Render)** : Un service d'hébergement où l'application sera déployée, avec un webhook de déploiement configuré pour être déclenché automatiquement.

#### Étapes Nécessaires pour le Déploiement

Suivez ces étapes pour assurer un déploiement réussi :

1. **Configurer les Secrets GitHub** : 
   - Accédez aux paramètres de votre dépôt GitHub, puis allez dans la section "Secrets and variables > Actions secrets".
   - Ajoutez les secrets `SECRET_KEY`, `DOCKER_HUB_USERNAME`, `DOCKER_HUB_PASSWORD`, et `RENDER_DEPLOY_HOOK_URL` avec leurs valeurs respectives.

2. **Vérifier la Configuration Docker** :
   - Assurez-vous que le fichier `Dockerfile` à la racine du projet est correctement configuré pour construire l'image Docker de l'application.
   - Le fichier doit inclure toutes les dépendances et les configurations nécessaires pour que l'application fonctionne correctement dans un environnement conteneurisé.

3. **Déclencher le Déploiement** :
   - Poussez vos modifications sur la branche `master` ou fusionnez une pull request vers `master`.
   - La pipeline CI/CD s'exécutera automatiquement :
     - Les tests seront d'abord lancés pour vérifier l'intégrité du code.
     - Ensuite, une image Docker sera construite et poussée sur Docker Hub.
     - Enfin, l'application sera déployée sur Render en utilisant le webhook de déploiement.

4. **Vérifier le Déploiement** :
   - Accédez à l'URL de votre application sur Render pour vous assurer que le déploiement s'est effectué correctement et que l'application fonctionne comme attendu.

En suivant ces instructions, le successeur pourra déployer l'application de manière fiable et efficace, en garantissant une continuité dans le processus de livraison de la solution.
