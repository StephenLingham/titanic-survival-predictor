import os

import pymongo
from pymongo.errors import PyMongoError

_mongo_uri = os.getenv("MONGODB_URI")
_memory_store = []

if _mongo_uri and _mongo_uri != "[ADD_MONGODB_URI_HERE]":
    client = pymongo.MongoClient(_mongo_uri, serverSelectionTimeoutMS=1000)
    db = client["titanic-database"]
    collection = db["titanic"]
else:
    client = None
    db = None
    collection = None


def add(document):
    if collection is None:
        _memory_store.append(document.copy())
        return

    try:
        collection.insert_one(document)
    except PyMongoError:
        _memory_store.append(document.copy())


def getAll():
    if collection is None:
        return list(_memory_store)

    try:
        return list(db.titanic.find({}))
    except PyMongoError:
        return list(_memory_store)


def deleteAll():
    if collection is None:
        _memory_store.clear()
        return

    try:
        db.titanic.delete_many({})
    except PyMongoError:
        _memory_store.clear()


def printAll():
    allDocuments = getAll()

    for doc in allDocuments:
        print(doc)
