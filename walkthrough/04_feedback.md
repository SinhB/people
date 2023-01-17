# Feedback

Le manque d'expérience avec FastAPi et SQLAlchemy m’a fait prendre plus de temps que prévu mais c'était un bon entrainement et j'ai apprécié de faire cette petite application.

- Contrairement à ce que je prévoyais au début je n'ai pas géré la dockerisation, j'aurais surement dû le faire dès le début, ça sera à faire si l'application évolue.
- Les endpoints pourraient être mieux structurer et passer par une authentification sera obligatoire par la suite.
- Je n'ai pas mis beaucoup l'accent sur la gestion d'erreur non plus, je suis passé par la validation que me donne `pydantic` mais il y a encore pas mal de travail cotée exception et sur les différentes réponses de l'API.
- Utiliser une autre DB telle que postgressql aurait été mieux mais avec l'architecture actuelle, l'implementation d'un repository propre à Postgres ne devrait pas être trop compliquer.
- Je pensais aussi Alembic pour les migrations mais je manque de temps pour le faire
- Utiliser `poetry` pour le management de package serait une idée pour la suite

Merci pour la lecture et le sujet :)