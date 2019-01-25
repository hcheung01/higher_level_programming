#!/usr/bin/python3
"""
commits history
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    name = argv[2]
    repo = argv[1]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(name,
                                                                         repo))
    for l in range(10):
        dicts = r.json()[l]
        author = dicts.get('commit').get('author').get('name')
        sha = dicts.get('sha')
        print("{}: {}".format(sha, author))
