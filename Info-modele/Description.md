### EuroMillions est un jeu de loterie dans lequel les joueurs des pays européens participants s'amusent à gagner d'énormes jackpots qui changent la vie. Le but du jeu est de choisisir cinq numéros de 1 à 50 et deux numéros Lucky Star de 1 à 12, sur les quels le gain est prononcé .

En utilisant les données des jeux passé, nous allons proposer un modèle de machine learning et intégrer à DVC pour versionner nos données.

La base de données contient 1 363 combinaisons de numeros compris entre 1 et 50 et de Lucky Star. 

**L'objectif est de prédire le jackpot ou le gain à partir des combinaisons de numéros**

#### Le dataset

L'entête 

 - Draw Date : date et heure de tirage
 - Winning Numbers : Numéros de gagnant
 - Bonus # : bonus associé aux numéros tirés
 - Extra # 
 - Jackpot : valeur du gains
 - Outcome : résultat du jeu

 - Draw Date : format date
 - Winning Numbers : format numerique
 - Bonus # : format numerique
 - Extra # : format numerique
 - Jackpot : format numerique
 - Outcome : format categoriel

Nombre d'individus: 1 363

#### Problème de machine learning

-Apprentissage supervisé
    -Regression 
        Linear
        Random Forest
        Decision Tree
        Score Vector Machine 


## https://www.kaggle.com/emfhal/euromillionsireland/