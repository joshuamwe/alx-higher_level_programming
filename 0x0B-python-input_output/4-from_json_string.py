#!/usr/bin/python3
"""module converting object(Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """returns object rep by JSON string"""
    return (json.loads(my_str))
