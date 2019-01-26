#!/usr/bin/python3
"""
Takes in a string and sends a search request to Star Wars API
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = 'https://swapi.co/api/people/'
    payload = {'search': argv[1]}
    s = requests.Session()
    res = s.get(url, params=payload).json()
    print("Number of results: {}".format(res['count']))
    while url:
        res = s.get(url, params=payload).json()
        for n in res['results']:
            print(n['name'])
            for film in n['films']:
                movie = s.get(film).json()
                print("\t{}".format(movie['title']))
        url = res['next']
        payload = {}
