#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)

    if sentence == "":
        return n, None
    else:
        return n, sentence[0]
