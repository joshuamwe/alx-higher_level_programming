#!/usr/bin/python3
"""module creates obj from JSON file"""
import json


def load_from_json_file(filename):
    """returns object from JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
