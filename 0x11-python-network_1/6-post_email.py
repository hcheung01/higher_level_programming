#!/usr/bin/python3
"""
Script that takes in a URL, email address, sends a POST request with email param
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
