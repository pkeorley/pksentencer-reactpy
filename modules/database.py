from pymongo import MongoClient


class Database:
    def __init__(self):
        self.cluster = MongoClient(
            (
                "MONGO_URL"
            )
        )
        self.economic = self.get_collection("economic")

    def get_collection(self, collection_name: str):
        return self.cluster.website[collection_name]
