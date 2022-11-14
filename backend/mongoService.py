import pymongo

client = pymongo.MongoClient("[ADD_MONGODB_URI_HERE]")

db = client["titanic-database"]

collection = db["titanic"]

def add(document):
    collection.insert_one(document)

def getAll():
    return list(db.titanic.find({}))

def deleteAll():
    db.titanic.delete_many({})

def printAll():
    allDocuments = getAll()

    for doc in allDocuments:
        print(doc)
