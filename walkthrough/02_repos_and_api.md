# Repository

Je decide de partir sur une architecture hexagonale et je commence donc à construire un repository, celui-ci se nommera `PeopleRepository` et aura des méthodes permettant à la réalisation des usent cases, c'est un peu straightforward, je pourrais écrire des méthodes plus génériques et passer par la gestion des usent cases entre les couches interfacent et domaine.

Un seul repository suffit pour l'instant, j'en profite pour implementer directement la version SQLite de ce repository en passant par `SQLAlchemy`.
Ce n'est pas très TDD tout ça ... mais je finis d'implementer les méthodes et j'ai maintenant envie d'implementer mon premier endpoint et tester le workflow entier.

# API

Comme je l'ai dit pendant mon analyse je ne fais pas de système d'authentification pour l'instant (ça impliquerait une base user, et tous les use cases de connexion qui vont avec). Mais ça reste un point indispensable si l'application évolue.

Je commence donc par implementer mon premier endpoint (le poste qui permettra aussi de provisioner la base de données.
Je passe par des BaseModel de `pydantic` pour la validation mais je ne gère pas les `personnes` en double dans la base, c'est un risque, je note ça pour plus tard mais je garde ce fonctionnement pour l'instant.

Après le test du workflow réussi du premier endpoint, j'en profite pour implementer les 3 autres (les méthodes du repo sont déjà prêtes, ça devrait aller assez vite).
Finalement je perds pas mal de temps sur le naming et les routes de mes endpoints, je ne suis pas entièrement satisfait.

Le fonctionnement des endpoints est assez précis et je pourrais en écrire des assez génériques avec des filtres/paramètres qui répondront au besoin, je decide quand même de me restreindre au fonctionnement attendu, chaque endpoint ne fera donc qu'une chose.

Je mens un peu car celui pour la répartition des genres par pays accepte un query en paramètres (`country`) qui permettent de faire un filtre sur le pays sélectionné.

```
@router.get("/people/gender/")
async def get_gender_repartition(
    country: str = Query(None),
    people_repo: PeopleRepository = Depends(get_people_repository),
) -> list[GenderRepartition]:
```

Je ne suis pas encore très à l'aise avec SQLAlchemy et l'asynchrone, j'ai passé plus de temps que prévu a cause de ça, mais c'est toujours bon à prendre.
Ajouter de la pagination et du throttling sur les endpoints serait bien aussi, je garde ça pour la suite si j'ai du temps.

Il faut quand même tester tout ça et je commence (il était temps :')) donc à écrire des [tests](/walkthrough/03_testing.md) ...