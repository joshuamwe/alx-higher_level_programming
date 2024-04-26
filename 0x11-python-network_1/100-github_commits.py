#!/usr/bin/python3
"""
lists 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
uses the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Prints all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys

if __name__ == '__main__':
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            owner_name, repository_name)
    r = requests.get(url)

    if r.status_code != 200:
        print("Request failed. Status code:", r.status_code)
        sys.exit()

    try:
        json_response = r.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()

    if not json_response:
        print("No commits found for the specified repository and owner")
        sys.exit()

    for commit in json_response[:10]:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
