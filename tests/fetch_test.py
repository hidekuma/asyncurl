import unittest
import requests
from collections.abc import Iterable
from asyncurl.fetch import AsyncURLFetch
from asyncurl.session import AsyncURLSession

TEST_URL ='http://github.com'
TEST_URLS = [
    TEST_URL
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

    def test_parallel_fetch_with_session(self):
        print('-------- [with session] ----------')
        fetch = AsyncURLFetch()
        session = AsyncURLSession()
        session.fetch_url = TEST_URL
        session.fetch_method = 'GET'
        session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        fetch.queue.put_nowait(session)
        print(fetch.parallel().results)

if __name__ == '__main__':
    unittest.main()
