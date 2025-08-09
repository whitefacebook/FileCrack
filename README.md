# Crack2.0 🔓💻


## 📌 Présentation
**Crack2.0** est un outil de *brute force* spécialisé dans le décryptage de fichiers **ZIP** et **RAR** protégés par mot de passe.  
Il utilise une **attaque par dictionnaire** et affiche en direct :
- Le mot de passe testé
- La vitesse (pwd/s)
- Le temps estimé restant

🎨 **Style visuel :**  
Thème **Anonymous / Matrix** avec effet d’affichage et couleurs dynamiques.

---

## ⚙️ Fonctionnalités
- 🔑 Crack de fichiers **ZIP**
- 🔑 Crack de fichiers **RAR**
- 📂 Wordlist par défaut (`password.txt`)
- 📂 Ajout possible d'une **wordlist personnalisée**
- ⏳ Calcul de la **vitesse** et du **temps restant**
- 🛡 Gestion propre des erreurs et **arrêt par Ctrl+C**
- 🎨 Bannière *Matrix Style* animée

---

## 📥 Installation

### 1. Installer Python et dépendances
Sous **Termux** :
```bash
pkg update && pkg upgrade
pkg install python git
pip install rarfile

git clone https://github.com/whitefacebook/FileCrack.git

Sous Linux :

sudo apt update && sudo apt install python3 python3-pip
pip3 install rarfile

git clone https://github.com/whitefacebook/FileCrack.git

▶️ Utilisation

python crack2.0.py

Ensuite :

1. Entrez le chemin du fichier à cracker (ZIP ou RAR)


2. Indiquez votre wordlist personnalisée ou laissez vide pour utiliser password.txt




📂 Exemple d’exécution

Chemin du fichier (ZIP ou RAR) : /storage/emulated/0/Download/fichier.zip
Chemin de votre wordlist (laisser vide si aucune) : /storage/emulated/0/Download/wordlist.txt
[INFO] 1200 mots de passe à tester...
▶ [0] admin | 350.50 pwd/s | Restant: 3.5s



🛠 Dépendances

Python 3.x

Module rarfile

Module zipfile (inclus par défaut)

Wordlist (password.txt par défaut)



⚠️ Avertissement

Cet outil est strictement à usage légal et éthique :

> N’utilisez Crack2.0 que sur vos propres fichiers ou avec l'autorisation explicite du propriétaire.



👤 Auteur

WHITE 404 GHz
Groupe Anonymous 404 RDC
Éthique Hacker • Sécurité Offensive • Cyber Résilience
