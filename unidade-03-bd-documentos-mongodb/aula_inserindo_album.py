import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

json_string = '{"nome" : "OLLYVER Somewhere Far Beyond", "dataLancamento" : "1992-05-30", "duracao" : "3328", "artista" : {"nome" : "Blind Guardian"}}'

album = json.loads(json_string)

db.albuns.insert(album)
