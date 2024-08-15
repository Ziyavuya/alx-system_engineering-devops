#!/usr/bin/python3
"""
Module to query subscribers on a given Reddit subreddit.

This module uses the Reddit API to fetch the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0

    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    if results:
        return results.get("subscribers")
    else:
        return 0
