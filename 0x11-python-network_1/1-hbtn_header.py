#!/usr/bin/python3
"""
script to fetch header
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from sys import argv

    req = Request(argv[1])
    with urlopen(req) as res:
        header = res.info()
        print(header['X-Request-Id'])
