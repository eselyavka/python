#!/usr/bin/env python

import unittest
import time
from collections import defaultdict


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_dict = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append(tuple([time.time(), tweetId]))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        follow = self.follow_dict.get(userId, set()).union(set([userId]))
        h = []
        for fid in follow:
            for tweet in self.tweets[fid]:
                h.append(tweet)
        h.sort(key=lambda t: t[0], reverse=True)

        return [t[1] for t in h[:10]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        try:
            self.follow_dict[followerId].remove(followeeId)
        except KeyError:
            pass


class TestSolution(unittest.TestCase):

    def test_Twitter(self):
        twitter = Twitter()
        actual = []
        actual.append(twitter.postTweet(1, 5))
        actual.append(twitter.getNewsFeed(1))
        actual.append(twitter.follow(1, 2))
        actual.append(twitter.postTweet(2, 6))
        actual.append(twitter.getNewsFeed(1))
        actual.append(twitter.unfollow(1, 2))
        actual.append(twitter.getNewsFeed(1))

        self.assertListEqual(actual, [None, [5], None, None, [6, 5], None, [5]])


if __name__ == '__main__':
    unittest.main()
