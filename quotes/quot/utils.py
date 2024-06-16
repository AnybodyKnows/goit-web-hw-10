from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        host="mongodb+srv://goittestdb:1234@cluster0.goh2ue4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client.HW08

    return db
