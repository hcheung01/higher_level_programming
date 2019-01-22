#!/usr/bin/python3
"""
Scripts that takes in a string and sends a search request to the Star Wars API
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get("https://swapi.co/api/people", params={'search': argv[1]})
    file = r.json()
    results = file['results']
    count = file['count']
    print("Number of results: {}".format(count))
    for arg in results:
        print(arg['name'])
