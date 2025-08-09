import zipfile
import os
import time
import sys
import zlib
import random
import rarfile  # Module pour gérer les fichiers RAR

# === Couleurs style Anonymous/Matrix ===
R = "\033[1;31m"  
G = "\033[1;32m"  
Y = "\033[1;33m"  
B = "\033[1;34m"  
M = "\033[1;35m"  
C = "\033[1;36m"  
W = "\033[1;37m"  
RESET = "\033[0m"

# === Effet Matrix pour la bannière ===
def matrix_text(text, delay=0.01):
    for char in text:
        sys.stdout.write(G + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# === Bannière avancée Crack2.0 ===
def banner():
    os.system("clear")
    matrix_text("""
██████╗ ██████╗  █████╗  ██████╗██╗  ██╗    ██████╗  ██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔═══██╗
██║  ██║██████╔╝███████║██║     █████╔╝     ██████╔╝██║   ██║
██║  ██║██╔═══╝ ██╔══██║██║     ██╔═██╗     ██╔═══╝ ██║   ██║
██████╔╝██║     ██║  ██║╚██████╗██║  ██╗    ██║     ╚██████╔╝
╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ 
             CRACK2.0  |  By WHITE 404 GHz
    """, delay=0.001)
    print(f"{C}Éthique Hacker • Sécurité Offensive • Couleurs Matrix{RESET}\n")
    time.sleep(0.5)

# === Charger les wordlists ===
def load_wordlist(default_path, custom_path=None):
    passwords = []
    if os.path.isfile(default_path):
        with open(default_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords += [line.strip() for line in f if line.strip()]
    else:
        print(f"{R}[!] Wordlist par défaut introuvable.{RESET}")
    if custom_path and os.path.isfile(custom_path):
        with open(custom_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords += [line.strip() for line in f if line.strip()]
    return list(dict.fromkeys(passwords))

# === Crack ZIP ===
def crack_zip(zip_path, wordlist):
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except zipfile.BadZipFile:
        print(f"{R}[ERREUR] Fichier ZIP invalide.{RESET}")
        return
    total = len(wordlist)
    print(f"{Y}[INFO] {G}{total}{Y} mots de passe à tester...{RESET}")
    start_time = time.time()
    for tested, password in enumerate(wordlist, start=1):
        elapsed = time.time() - start_time
        speed = tested / elapsed if elapsed > 0 else 0
        remaining = (total - tested) / speed if speed > 0 else 0
        sys.stdout.write(f"{G}▶ [{random.choice('01')}]{RESET} {C}{password}{RESET} | {G}{speed:.2f} pwd/s{RESET} | {Y}Restant: {remaining:.1f}s{RESET}    \r")
        sys.stdout.flush()
        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            print(f"\n\n{G}[SUCCÈS] Mot de passe trouvé : {W}{password}{RESET}")
            print(f"{C}Temps total : {elapsed:.2f} secondes{RESET}")
            return
        except:
            pass
    print(f"\n{R}[ECHEC] Aucun mot de passe trouvé.{RESET}")

# === Crack RAR ===
def crack_rar(rar_path, wordlist):
    try:
        rar_file = rarfile.RarFile(rar_path)
    except rarfile.BadRarFile:
        print(f"{R}[ERREUR] Fichier RAR invalide.{RESET}")
        return
    total = len(wordlist)
    print(f"{Y}[INFO] {G}{total}{Y} mots de passe à tester...{RESET}")
    start_time = time.time()
    for tested, password in enumerate(wordlist, start=1):
        elapsed = time.time() - start_time
        speed = tested / elapsed if elapsed > 0 else 0
        remaining = (total - tested) / speed if speed > 0 else 0
        sys.stdout.write(f"{M}▶ [{random.choice('01')}]{RESET} {C}{password}{RESET} | {G}{speed:.2f} pwd/s{RESET} | {Y}Restant: {remaining:.1f}s{RESET}    \r")
        sys.stdout.flush()
        try:
            rar_file.extractall(pwd=password)
            print(f"\n\n{G}[SUCCÈS] Mot de passe trouvé : {W}{password}{RESET}")
            print(f"{C}Temps total : {elapsed:.2f} secondes{RESET}")
            return
        except:
            pass
    print(f"\n{R}[ECHEC] Aucun mot de passe trouvé.{RESET}")

# === Main ===
try:
    banner()
    file_path = input(f"{B}Chemin du fichier (ZIP ou RAR) : {RESET}").strip()
    custom_wordlist = input(f"{B}Chemin de votre wordlist (laisser vide si aucune) : {RESET}").strip()
    default_wordlist = "password.txt"
    wordlist = load_wordlist(default_wordlist, custom_wordlist if custom_wordlist else None)

    if wordlist:
        if file_path.lower().endswith(".zip"):
            crack_zip(file_path, wordlist)
        elif file_path.lower().endswith(".rar"):
            crack_rar(file_path, wordlist)
        else:
            print(f"{R}[ERREUR] Format de fichier non supporté.{RESET}")
    else:
        print(f"{R}[ERREUR] Aucune wordlist disponible.{RESET}")

except KeyboardInterrupt:
    print(f"\n{Y}[INFO] Au revoir et à très bientôt, camarade hacker.{RESET}")
    sys.exit()
except Exception as e:
    print(f"\n{R}[ERREUR] {e}{RESET}")
    sys.exit()
