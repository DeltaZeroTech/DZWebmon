# DZWebMon

**DZWebMon** est un script Python permettant de surveiller des pages web pour détecter tout changement de contenu. Lorsqu'un changement est détecté, le script envoie une notification via Telegram et enregistre les modifications dans un fichier pour un suivi historique.

## 🚀 Fonctionnalités

- **Surveillance automatique** : Le script surveille une page web à intervalles réguliers (configurable).
- **Notifications Telegram** : Lorsqu'un changement est détecté, une notification est envoyée via Telegram.
- **Sauvegarde des changements** : Les modifications détectées sont enregistrées dans un fichier texte pour une référence future.
- **Gestion des messages longs** : Si un changement génère un message de plus de 4096 caractères (la limite de Telegram), le message est automatiquement divisé et envoyé en plusieurs parties.

## 🛠️ Prérequis

- Python 3.7 ou version supérieure
- Un compte Telegram et un bot configuré via **BotFather**

## 🛑 Installation

1. **Clonez le dépôt** :

   ```bash
   git clone https://github.com/DeltaZeroTech/DZWebmon.git
   cd DZWebmon
   ```

2. **Installez les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Créez un fichier `.env`** pour stocker les informations sensibles (comme le Token Telegram et l'ID du chat). Placez ce fichier à la racine du projet.

   Exemple de contenu du fichier `.env` :

   ```bash
   TELEGRAM_BOT_TOKEN=123456789:ABCDefghijklmnopqrstuvwxyz012345
   TELEGRAM_CHAT_ID=987654321
   ```

   - **`TELEGRAM_BOT_TOKEN`** : Le token API que vous avez obtenu via **BotFather**.
   - **`TELEGRAM_CHAT_ID`** : L'ID de votre chat personnel ou de votre groupe Telegram.

## 📲 Configuration du bot Telegram

### Étapes pour configurer un bot Telegram :

1. Recherchez **BotFather** dans l'application Telegram et démarrez une conversation.
2. Utilisez la commande `/newbot` pour créer un nouveau bot, suivez les instructions et obtenez un **token**.
3. Ajoutez le bot à un groupe si vous souhaitez que le bot envoie des notifications dans un groupe.
4. Utilisez l'API `getUpdates` pour obtenir votre **chat_id** :
   Remplacez `<BOT_TOKEN>` par le token que vous avez obtenu de BotFather :

   ```bash
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   ```

5. Envoyez un message dans le chat ou le groupe où le bot est présent, puis récupérez le **chat_id** dans la réponse JSON.

## 🚀 Utilisation

1. Modifiez l'URL de la page web à surveiller dans le script :

   ```python
   url = "https://exemple.com/page"
   ```

2. Lancer le script pour démarrer la surveillance :

   ```bash
   python DZWebMon.py
   ```

3. Le script surveillera la page toutes les 60 secondes par défaut. Vous pouvez ajuster l'intervalle en modifiant la variable `interval` dans le code.

### ✂️ Fonctionnalité de division des messages

Si un changement génère un message de plus de 4096 caractères, le message sera automatiquement divisé en plusieurs parties pour éviter les erreurs liées à la longueur maximale des messages Telegram.

## 📁 Structure des fichiers

- **`DZWebMon.py`** : Le script principal qui surveille les pages et envoie des notifications.
- **`.env`** : Le fichier de configuration contenant le token Telegram et l'ID du chat (ce fichier n'est pas inclus dans le dépôt Git pour des raisons de sécurité).
- **`requirements.txt`** : Fichier contenant la liste des dépendances nécessaires.

## 📤 Exemple de sortie

```
Surveillance de la page : https://exemple.com/page
Changements détectés sur https://exemple.com/page !
- Ligne 1 modifiée
+ Ligne 2 modifiée
Notification envoyée avec succès à 987654321.
```

## 📦 Dépendances

Les dépendances du projet sont spécifiées dans le fichier `requirements.txt`. Vous pouvez les installer avec la commande suivante :

```bash
pip install -r requirements.txt
```

Les principales dépendances sont :

- **`requests`** : Pour récupérer le contenu des pages web.
- **`python-telegram-bot`** : Pour envoyer les notifications via Telegram.
- **`python-dotenv`** : Pour gérer les variables d'environnement.

## 📜 Licence

Ce projet est sous licence MIT.
