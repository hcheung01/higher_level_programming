#!/usr/bin/python3
"""
script to take in a URL input, sends a request to the URL, display response
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(page.text)
