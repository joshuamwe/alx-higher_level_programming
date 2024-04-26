#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        content = response.read()

        response_body = {
                'type': type(content),
                'content': content,
                'utf8 content': content.decode('utf-8')
                }

        print("Body response:")
        print("\t- type: {}".format(response_body['type']))
        print("\t- content: {}".format(response_body['content']))
        print("\t- utf8 content: {}".format(response_body['utf8 content']))
