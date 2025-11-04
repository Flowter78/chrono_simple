# Chrono README

## Prérequis
- Python doit être installé et accessible via la variable PATH.
- Le dossier `C:\Users\flore\MesScripts` doit être inclus dans la variable d'environnement `%PATH%`.
- (Optionnel) Vérifier que l'extension `.VBS` est listée dans `PATHEXT`.

## Installation
1. Copier `chrono.py` dans :  
   `C:\Users\flore\MesScripts`
2. **VBScript** (recommandé) :
   ```vbscript
   Set WshShell = CreateObject("WScript.Shell")
   WshShell.Run "python ""C:\\Users\\flore\\MesScripts\\chrono.py""", 0
   ```
   Placer `chrono.vbs` dans un dossier du PATH permet de lancer le chrono en tapant `chrono`.  
   
3. **PowerShell** (alternative) :
   ```powershell
   Start-Process -FilePath python `
     -ArgumentList 'C:\\Users\\flore\\MesScripts\\chrono.py' `
     -WindowStyle Hidden
   ```
   Créer un raccourci Windows (.lnk) dont la cible est :
   ```
   C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -ExecutionPolicy Bypass -File "C:\\Users\\flore\\MesScripts\\chrono.ps1"
   ```
   Nommer le raccourci `chrono` et le placer dans un dossier du PATH.

## Utilisation
- Ouvrir **CMD** ou **PowerShell** et taper :
  ```bash
  chrono
  ```

## Lancer le script au démarrage 

mettre un raccourcis avec la cible suivante : C:\Windows\System32\wscript.exe "C:\Users\flore\MesScripts\chrono_simple\chrono.vbs"
Dans le dossier suivant: C:\Users\flore\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
---
[Arrondir coin d'une image](https://round-corner.imageonline.co/fr/)  
[Convertir png vers ico](https://convertio.co/fr/download/c8112ef476884f0f935c3482eeb6541702f5e2/)  
[clavier+ pour les raccourcis clavier](https://github.com/guilryder/clavier-plus)
[Création d'un executable à partir d'un script vbs](snapfiles.com/get/vbstoexe.html)
