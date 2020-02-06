#!/usr/bin/python3
"""
Recurse hot articles on Reddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Get top posts on reddit
    """
    fake_agent = 'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62'
    base_url = 'http://www.reddit.com/'
    resource = 'r/{}/hot.json?limit=100&after={}'\
        .format(subreddit, "" if not hot_list else hot_list[-1])
    req = requests.get(base_url + resource,
                       headers={'User-Agent': fake_agent})

    if req.status_code != 404:
        out = req.json()
        childrens = out.get('data').get('children')
        after = out.get('data').get('after')
        hot_list += list(map(lambda x: 't3_' + x.get('data').get('id'),
                             childrens))

        if after is None:
            return hot_list
        else:
            recurse(subreddit, hot_list)
    else:
        return None
