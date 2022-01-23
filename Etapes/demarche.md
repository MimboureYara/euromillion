## 1) Création du dossier de travail

## 2) Description du problème

## 3) Configuration du depot de distant

`git init` <!-- initialiser un depot git 
`git checkout -b V1.0` <!-- créer une brache et se switcher à la branche
`dvc init` <!-- initialiser un depot data version control
    
`dvc remote add -d depotdis /Users/hp/pjeuromillion/dossier-distant-dvc -f` <!-- ajout de stockage distant dans un dossier local

`dvc add /Users/hp/pjeuromillion/data/euro-millions-ireland.csv`<!-- versionner notre dataset par DVC

`dvc push` <!-- Pousser les changements sur les données à ajoutées vers notre stockage distant

`git remote add <chemin-dossier_dvc> <lien>` <!-- ajouter un depot Git distant (Github par exemple)

`dvc remote add -d dossier-distant-dvc gdrive://1uBeDsU_JnN2ZDuwVsizenzx7CGFhEcza -f` <!--Ajouter un depot drive distant (google drive)

`dvc push`

`dvc remote add -d dossier-distant-dvc https://github.com/MimboureYara/euromillion.git -f` <!--Ajouter un depot drive distant (github)

`dvc push`

## 4) Initiation de l'environnement pipenv
`pipenv install` <!-- installation et creation des fichiers 
-__Pipfile__: contenu modifiable
-__Pipfile.lock__

## 5) Modification du fichier pipfile pour ajout des dependances du projet
`pipenv install --dev` <!--installation des dependances definie dans le fichier Pipfile

## 5) 