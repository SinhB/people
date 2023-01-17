# Analyse

Hello, 
tu trouveras dans ce dossier le fruit de mon raisonnement, les étapes par lesquelles je suis passé, les choix que j'ai du faire et les questions que je me suis posé pendant ce test.

D’après le test que tu m'as envoyé, le but est de:

- Créer un service backend qui va exposer une api. Tu m'avais parlé à l'oral de FastApi, je ne le retrouve pas dans le mail mais je vais rester là dessus pour le framework.
- Stocker les données dans une base de données SQL. Je pense partir sur du SQLite pour la simplicité / rapidité de mise en place.
- Créer 4 endpoints, 1 POST et 3 GET a première vue.

Tu ne me parle pas de déploiement, ni de sécurité (authentification, throttling, etc).

Je met donc ça de côté pour l'instant mais je m'y attaquerais peut être si j'ai du temps. (Je n'oublie pas ce que tu m'as dit pendant notre conversation, je ne compte donc pas passer trop de temps sur le sujet et me contenter de l’essentiel pour l'instant.)

Je pars donc sur une application FastApi branché a une db SQLite.

Pas d’authentification au niveau de l’API, je ne pense donc pas créer de table utilisateur pour l'instant.

Je pense utiliser des containers docker avec docker-compose.

J'ai trois services qui me viennent a l'esprit:

- Un service api
- Un service pour la DB
- Un service pour les migrations (en utilisant Alembic ?)

## API

Concernant l'API tu me demandes 4 endpoints. 

Je n'ai pas vraiment d'informations mis a part le format du endpoint POST. J'ai donc le champ libre sur les routes a créer.

Les 4 endpoints traitent des `people`, je pense donc construire ma route a partir de `/people/`

- POST `/people`
- GET `/people/average/age/country`
- GET `/people/gender/repartition`
- GET `/people/count/country`


Je m'attaque au setup de mon app -> [setup](/walkthrough/01_setup.md)