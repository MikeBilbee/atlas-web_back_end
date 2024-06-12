#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient()
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:") 
    method_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in method_list: 
        print("\tmethod {}: {}".format(method, collection.count_documents({"method": method})))
    print("{} status check".format(collection.count_documents({"path": "/status"})))