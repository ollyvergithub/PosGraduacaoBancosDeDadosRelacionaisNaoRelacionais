from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
db = GraphDatabase("http://localhost:7474", username="neo4j", password="olotgrafo")

# Obtendo todos os usuário que Bob segue na rede
q = 'MATCH (u1:Usuario)-[r:follows]->(u2:Usuario) WHERE u1.name="Bob" RETURN u1, type(r), u2'

results = db.query(q, returns=(client.Node, str, client.Node))

for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))

# saída:
# (Bob)-[follows]->(Alice)

