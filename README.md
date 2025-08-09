# Crack2.0 🔓💻



# 📌 Présentation
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
