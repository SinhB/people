# Test

Bon au début je pensais partir sur du TDD au vu des usent cases plutôt simples mais le fait d'avoir voulu tester ma db et le workflow entier une première fois ma amener à ce point, tous les endpoints implémenté et encore aucun test d'écrit ...

Je vais utiliser `pytest` et `starlette` pour pouvoir tester les endpoints

Je commence par écrire les tests du repository SQLite, je passe par une DB en RAM pour cela.
Les tests ne sont pas très poussés mais j'arrive à tester chaque méthode, le fait d'être en asynchrone me fait perdre un peu de temps car je dois lire pas mal de doc.

Une fois les tests passes je commence les ceux des endpoints et je mock le repository pour ne pas impacter la DB, je test seulement le fait que mes endpoints renvoient format attendu.

Je ne couvre pas tout avec mes tests mais j'ai déjà une base.

Je pense m'arrêter là pour le moment, j'ai déjà passé pas mal de temps donc place au [feedback](/walkthrough/04_feedback.md)
