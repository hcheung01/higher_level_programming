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
    for li in range(10):
        print("{}:".format(r.json()[li].get('sha')),
              r.json()[li].get('commit').get('author').get('name'))
