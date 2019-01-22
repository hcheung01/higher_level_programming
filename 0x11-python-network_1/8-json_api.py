#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to URL with letter param
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    if len(argv) == 1:
        q = ''
    else:
        q = argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        out = r.json()
        if out:
            print('[{}] {}'.format(out['id'], out['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
