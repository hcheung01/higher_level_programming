#!/usr/bin/python3
"""
sha + author commits history
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    if (len(argv) == 3):
        name = argv[2]
        repo = argv[1]
        r = requests.get('https://api.github.com/repos/{}/{}/commits'
                         .format(name, repo))
        r = r.json()
        for i in range(10):
            name = r[i]['commit']['author']['name']
            sha = r[i]['sha']
            print("{}: {}".format(sha, name))
