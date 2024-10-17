# DZWebmon
DZWebMon est un script Python qui permet de surveiller des pages web afin de détecter tout changement de contenu. Il envoie des notifications via Telegram et enregistre les modifications dans un fichier pour un suivi historique.

Fonctionnalités

Surveillance automatique d'une page web à des intervalles réguliers.
Notification via Telegram lorsqu'un changement est détecté.
Sauvegarde des changements dans un fichier texte pour référence future.
Gestion des messages trop longs pour Telegram en les divisant en plusieurs parties.

Prérequis

Python 3.7 ou version supérieure
Un compte Telegram et un bot configuré via BotFather

Installation

Clonez le dépôt :
bash

git clone https://github.com/votre-utilisateur/web-monitor.git cd web-monitor

Installez les dépendances nécessaires :

bash

pip install -r requirements.txt

Créez un fichier .env pour stocker les informations de configuration sensibles (Token du bot Telegram et ID du chat). Ce fichier .env doit être placé dans la racine du projet.

Exemple de contenu du fichier .env :

bash

TELEGRAM_BOT_TOKEN=123456789:ABCDefghijklmnopqrstuvwxyz123456
TELEGRAM_CHAT_ID=987654321

    TELEGRAM_BOT_TOKEN : Le token API que vous avez obtenu via BotFather.
    TELEGRAM_CHAT_ID : L'ID de votre chat personnel ou de votre groupe Telegram.

Configuration du bot Telegram Étapes pour configurer un bot Telegram :

Recherchez BotFather dans l'application Telegram et démarrez une conversation.
Utilisez la commande /newbot pour créer un nouveau bot et suivez les instructions. Vous obtiendrez un token.
Ajoutez le bot à un groupe (si vous souhaitez que le bot envoie des notifications dans un groupe).
Utilisez l'API getUpdates pour récupérer le chat_id :
    Remplacez <BOT_TOKEN> par le token que vous avez obtenu :

    bash

    https://api.telegram.org/bot<BOT_TOKEN>/getUpdates

    Envoyez un message dans le chat ou le groupe où le bot est présent, et recherchez l'ID du chat dans la réponse JSON.

Utilisation

Modifiez l'URL de la page web à surveiller dans le script :

python

url = "https://exemple.com/page"

Lancer le script pour démarrer la surveillance :

bash

python DZWebMon.py

Le script surveillera la page toutes les 60 secondes par défaut. Vous pouvez ajuster l'intervalle en modifiant le paramètre interval dans le code.

Fonctionnalité de division des messages

Si un changement génère un message de plus de 4096 caractères (la limite de Telegram), le message sera automatiquement divisé en plusieurs parties et envoyé séparément pour éviter toute erreur liée à la taille des messages. Structure des fichiers

DZWebMon.py : Le script principal qui surveille les pages et envoie des notifications.
.env : Le fichier de configuration contenant le token Telegram et l'ID du chat (non inclus dans le dépôt Git pour des raisons de sécurité).
requirements.txt : Fichier contenant la liste des dépendances nécessaires.

Exemple de sortie

arduino

Surveillance de la page : https://exemple.com/ Changements détectés sur https://exemple.com/ ! Ligne 1 modifiée Ligne 2 modifiée Notification envoyée avec succès à 4564787998.

Dépendances

Les dépendances du projet sont spécifiées dans le fichier requirements.txt. Voici les principales bibliothèques utilisées :

requests
python-telegram-bot
python-dotenv

Vous pouvez les installer avec la commande suivante :

bash

pip install -r requirements.txt

Licence

Ce projet est sous licence MIT.
