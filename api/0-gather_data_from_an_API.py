#!/usr/bin/python3

"""
    The `Gather data from an API` module
"""


if __name__ == "__main__":

    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    user_name = (
        requests.get(
            f"https://jsonplaceholder.\
typicode.com/users/{argv[1]}"
        )
        .json()
        .get("name")
    )

    todos = requests.get(
        f"https://jsonplaceholder.typicode.\
com/todos?userId={argv[1]}"
    ).json()

    total = len(todos)
    completed = 0
    titles = ""
    for i in todos:
        if i["completed"]:
            completed += 1
            titles += "\t " + i.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(user_name, completed, total))

    if titles != "":
        print(titles[:-1])
