#!/usr/bin/python3
"""
Python script
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen

    req = Request('https://intranet.hbtn.io/status')
    with urlopen(req) as f:
        the_page = f.read()
        print('Body response:')
        print('\t- type: {}'.format(type(the_page)))
        print('\t- content: {}'.format(the_page))
        print('\t- utf8 content: {}'.format(the_page.decode('utf8')))
