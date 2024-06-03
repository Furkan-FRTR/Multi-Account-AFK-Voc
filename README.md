# Multi-Account-AFK-Voc by ___furkan___

Ce script permet de connecter plusieurs comptes Discord à un canal vocal en utilisant des tokens chaque compte se connecte en mode muet et sourdine c'est un un script pour avoir des token en vocal en mass +100

## Prérequis

- Python 3.8+
- Les bibliothèques Python (voir fichier requirements.txt)

## Installation

1. Installez les dépendances :

pip install -r requirements.txt

2. Ajoutez les tokens des comptes Discord dans le fichier token.txt, un token par ligne :
token1
token2
token3

3. Lancer le script 
main.py

## Configuration
Modifiez les variables GUILD_ID et CHANNEL_ID dans le script principal pour correspondre à l'identifiant de votre serveur et du canal vocal où vous souhaitez connecter les comptes.
Remplacez par les identifiants de votre serveur (GUILD_ID) et canal vocal (CHANNEL_ID)
GUILD_ID = 3828284338432872782
CHANNEL_ID = 285832872872843

# Utilisation
Lancez le script principal :
<python main.py>
Le script validera les tokens et connectera chaque compte au canal vocal spécifié. Vous verrez dans la console les informations des comptes connectés.

# Fonctionnalités
Connexion de plusieurs comptes Discord à un canal vocal
Statut configuré en ligne, muet et sourdine par défaut
Serveur Flask pour garder le script actif (replit)

# Avertissement
L'utilisation de plusieurs comptes Discord pour automatiser des actions peut violer les conditions d'utilisation de Discord. Utilisez ce script de manière responsable et assurez-vous de respecter les règles de Discord.

# Contribuer
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des modifications que vous souhaitez apporter.

# Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Attention : Ce script est à des fins éducatives uniquement. L'utilisation de ce script de manière contraire aux conditions d'utilisation de Discord peut entraîner des sanctions sur votre compte.
