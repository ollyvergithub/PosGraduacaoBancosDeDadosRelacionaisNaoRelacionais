import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.aula

albuns = db.albuns.find({})

for album in albuns:
    print(album)

album = db.albuns.find_one({"nome": "OLLYVER Somewhere Far Beyond"})
print(f"\nImprimindo Album específico {album}")

artista = album['artista']['nome']
print(f"\nImprimindo Artista do Album específico {artista}")

