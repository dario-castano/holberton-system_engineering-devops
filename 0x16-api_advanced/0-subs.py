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
                       headers={'User-Agent': fake_agent}).json()

    if req is None or req.get('kind') == 'Listing':
        return 0
    elif req.get('kind') == 't5':
        return req.get('data').get('subscribers')
