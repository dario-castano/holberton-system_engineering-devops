#!/usr/bin/python3
"""
Search top ten hottest posts
"""
import requests


def top_ten(subreddit):
    """
    Get top posts on reddit
    """
    fake_agent = 'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62'
    base_url = 'http://www.reddit.com/'
    resource = 'r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(base_url + resource,
                       headers={'User-Agent': fake_agent})

    if req.status_code != 404:
        out = req.json()
        if out.get('data').get('dist') > 0:
            for post in out.get('data').get('children'):
                print(post.get('data').get('title'))
            return
    print('None')
    return
