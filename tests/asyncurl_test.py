import unittest
from asyncurl import asyncurl

TEST_URLS = [
    'http://localhost',
]

class AsnyncURLTest(unittest.TestCase):
    def test_parallel_fetch_1(self):
        print('-------- [return results] ----------')
        asycurl = asyncurl.AsyncURL()
        self.assertIsInstance(asycurl.parallel_fetch(TEST_URLS).results, list)
    
    def test_parallel_fetch_2(self):
        print('-------- [print results] ----------')
        asycurl = asyncurl.AsyncURL()
        asycurl.parallel_fetch(TEST_URLS).print_results()
    
    def test_parallel_fetch_3(self):
        print('-------- [with callback] ----------')
        asycurl = asyncurl.AsyncURL()
        asycurl.parallel_fetch(TEST_URLS, callback=lambda x: print('with callback : {0}'.format(x)))

if __name__ == '__main__':
    unittest.main()
