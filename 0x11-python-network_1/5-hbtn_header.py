#!/usr/bin/python3
"""
Python script for requests
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])
