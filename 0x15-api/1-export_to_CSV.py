#!/usr/bin/python3
"""Returns info on given employee with ID."""

import requests
import sys

if __name__ == "__main__":
    """Main function."""
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(link + "todos", params={"userId": sys.argv[1]}).json()
    completed = [task.get("title") for task in todo if task.get("completed")]

    with open("{}.csv".format(sys.argv[1]), "w") as f:
        [f.write('"{}","{}","{}","{}"\n'.format(
            sys.argv[1], user.get("username"), task.get(
                "completed"), task.get("title")
        )) for task in todo]
