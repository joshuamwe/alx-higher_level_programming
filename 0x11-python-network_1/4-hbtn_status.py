#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
using requests package
"""
import requests

if __name__ == "__main__":

    content = requests.get(
            "https://alx-intranet.hbtn.io/status")

    response_body = {
            'type': type(content.text),
            'content': content.text
            }

    print("Body response:")
    print("\t- type: {}".format(
        response_body.get('type')))
    print("\t- content: {}".format(
        response_body.get('content')))
