#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def log_stats():
    """Prints stats about Nginx logs stored in MongoDB."""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Count total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count occurrences of each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count occurrences of GET requests to /status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    log_stats()
