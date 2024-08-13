#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get, HTTPError

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if not isinstance(subreddit, str) or not subreddit:
        print("None")
        return

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = get(url, headers=user_agent, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        results = response.json()

        my_data = results.get('data', {}).get('children', [])

        if not my_data:
            print("None")
            return

        for i in my_data:
            print(i.get('data', {}).get('title', 'None'))

    except HTTPError:
        print("None")
    except Exception as e:
        print(f"None: {e}")
