#!/usr/bin/env python

import unittest
import hashlib

class Codec(object):

    def __init__(self):
        self._map = dict()
        self.prefix = 'http://tinyurl.com/'

    def encode(self, longUrl):
        url_hash = hashlib.sha256(longUrl).hexdigest()
        url_short = url_hash[:3] + url_hash[-3::]
        self._map[url_short] = longUrl
        return self.prefix + url_short

    def decode(self, shortUrl):
        return self._map[shortUrl.split('/')[-1]]

class TestCodec(unittest.TestCase):

    def test_encode_decode(self):
        longUrl = 'https://leetcode.com/problems/design-tinyurl'
        shortUrl = 'http://tinyurl.com/f86784'
        solution = Codec()
        self.assertEqual(solution.encode(longUrl), shortUrl)
        self.assertEqual(solution.decode(shortUrl), longUrl)
        self.assertEqual(solution.decode(solution.encode(longUrl)), longUrl)

if __name__ == '__main__':
    unittest.main()
