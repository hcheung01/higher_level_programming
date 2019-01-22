#!/usr/bin/python3
"""
script to take in a URL input, sends a request to the URL, display response
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    try:
        req = requests.get(argv[1])
        if req:
            print(req.content.decode('utf-8'))
        elif req.status_code >= 400:
            print("Error code: {}".format(req.status_code))
    except KeyError:
        pass
