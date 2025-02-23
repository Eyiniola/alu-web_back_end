#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient

def get_log_stats():
    """
    This function connects to a MongoDB database, retrieves statistics about Nginx logs
    stored in the 'nginx' collection, and prints the results in a specific format.
    """
    # Connect to MongoDB running on localhost at the default port 27017
    client = MongoClient('mongodb://localhost:27017/')
    
    # Access the 'logs' database
    db = client['logs']
    
    # Access the 'nginx' collection within the 'logs' database
    collection = db['nginx']

    # Get the total number of documents in the 'nginx' collection
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Define the HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    # Print the header for the methods section
    print("Methods:")
    
    # Iterate over each HTTP method and count the number of documents with that method
    for method in methods:
        # Count documents where the 'method' field matches the current method
        count = collection.count_documents({"method": method})
        # Print the count for the current method, indented with a tab
        print(f"    method {method}: {count}")

    # Count the number of documents where the method is 'GET' and the path is '/status'
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    # Print the count for status checks
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    # Entry point of the script: call the get_log_stats function
    get_log_stats()