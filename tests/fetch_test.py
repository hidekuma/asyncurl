import unittest
import requests
from collections.abc import Iterable
from asyncurl.fetch import AsyncURLFetch

TEST_URLS = [
    'http://github.com',
]

class AsyncURLFetchTest(unittest.TestCase):
    def test_instance(self):
        fetch = AsyncURLFetch()
        fetch.worker = 3
        self.assertEqual(fetch.worker, 3)

    def test_parallel_fetch_basic(self):
        print('-------- [return results] ----------')
        fetch = AsyncURLFetch()
        results = fetch.parallel(TEST_URLS).results
        print(results)
        self.assertIsInstance(results, Iterable)
    
    def test_parallel_fetch_with_callback(self):
        print('-------- [with callback] ----------')
        fetch = AsyncURLFetch()
        fetch.parallel(TEST_URLS, callback=lambda x: print('with callback : {0}'.format(x)))

    def test_parallel_fetch_with_queue(self):
        print('-------- [with queue] ----------')
        fetch = AsyncURLFetch()
        results = fetch.parallel(TEST_URLS, queue=True).results
        print(results)
        self.assertIsInstance(results, Iterable)

if __name__ == '__main__':
    unittest.main()
