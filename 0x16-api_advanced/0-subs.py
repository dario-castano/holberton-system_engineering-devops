#!/usr/bin/python3
"""
Search number of subscribers on reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get subscribers from Reddit
    """
    fake_agent = 'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62'
    base_url = 'http://www.reddit.com/'
    resource = 'r/{}/about.json'.format(subreddit)
    req = requests.get(base_url + resource,
                       headers={'User-Agent': fake_agent})

    if req.status_code != 404:
        out = req.json()
        if out.get('kind') == 't5':
            return out.get('data').get('subscribers')

    return 0
