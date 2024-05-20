#!/usr/bin/python3
"""Returns info on given employee with ID."""

import json
import requests

if __name__ == "__main__":
    """Main function."""
    link = "https://jsonplaceholder.typicode.com/"
    users = requests.get(link + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed"),
        } for task in requests.get(link + "todos",
                                   params={"userId": user.get("id")}
                                   ).json()
        ] for user in users}, f)
