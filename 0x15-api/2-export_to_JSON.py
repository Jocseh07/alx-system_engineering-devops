#!/usr/bin/python3
"""Returns info on given employee with ID."""

import json
import requests
import sys

if __name__ == "__main__":
    """Main function."""
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(link + "todos", params={"userId": sys.argv[1]}).json()
    completed = [task.get("title") for task in todo if task.get("completed")]

    with open("{}.json".format(sys.argv[1]), "w") as f:
        json.dump({sys.argv[1]: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in todo]}, f)
