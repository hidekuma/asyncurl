import unittest
from asyncurl import asyncurl

class AsnyncURLTest(unittest.TestCase):
    def test_parallel_fetch(self):
        urls = [
            'http://localhost',
        ]
        asycurl = asyncurl.AsyncURL()
        self.assertIsInstance(asycurl.parallel_fetch(urls).results, list)

if __name__ == '__main__':
    unittest.main()
