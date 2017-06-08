# Dossier chiffré

# Créer le dossier
* Installer `ecryptfs-utils`:
```
sudo apt-get install ecryptfs-utils
```
* Lancer la création :
```
ecryptfs-setup-private
``` 
* Compléter les champs
* Rendre le binaire exécutable :
```
sudo chmod +x /usr/share/ecryptfs-utils/ecryptfs-mount-private.desktop
```

# Déchiffrer le dossier
* Cliquer sur le lanceur dans `~/Private`
* Actualiser la vue du navigateur de fichier si besoin
OU
* Faire `ecryptfs-mount-private`

# Chiffrer le dossier
* Faire  `ecryptfs-umount-private`