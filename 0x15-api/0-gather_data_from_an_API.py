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
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)
    ))
    [print("\t {}".format(task)) for task in completed]
