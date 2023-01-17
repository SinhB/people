# Setup

Je commence l'installation de mon app:
- Virtualenv (je decide de partir sur du python 3.10, la 3.11 étant déjà sortie je préfère quand même prendre le moins de risque possible au niveau compatibilité)
- installation des dépendances, fastapi, pydantic, Sqlite

Après un premier `Hello World` réussi je commence à implementer les settings de connexion a la base de données. Je veux partir sur de l'asynchrone, je dois ajouter `aiosqlite` aux dépendances pour pouvoir gerer les sessions async avec SQLite.

## Model

Je n'ai eu aucune instruction concernant les modèles de données mises a par un input valide pour l'endpoint qui sera en charge de créer les personnes en base.
Je me base sur ce format et je pars sur l'idée de n'avoir qu'une seule table `Person` défini comme suit:

```
class Person(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String, index=True)
    country = Column(String, index=True)
```

Les champs `gender` et `country` sont des chaines de caractères, c'est intentionnel pour rester sur un modèle simple. `country` aurait pu très bien être un modèle a part entière et `gender` une liste de choix en enum, je garde ça dans un coin de ma tete pour la suite.

Une fois mon model de donne pret je passe a [la création de repos](/walkthrough/02_repos_and_api.md)