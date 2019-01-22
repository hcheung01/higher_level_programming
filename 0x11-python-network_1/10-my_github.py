#!/usr/bin/python3
"""
takes my Github credentials and uses the Github API to display my id
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    try:
        r = requests.get("https://api.github.com/user",
                         auth=(argv[1], argv[2]))
        file = r.json()
        print(file['id'])
    except:
        print('None')
