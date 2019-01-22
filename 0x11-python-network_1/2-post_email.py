#!/usr/bin/python3
"""
POST script
"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv
    import urllib.parse

    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    email = data.encode('ascii')
    req = Request(url, email)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode('utf8'))
