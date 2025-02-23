#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def get_log_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # Get the total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Get the count for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Get the count for method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    get_log_stats()