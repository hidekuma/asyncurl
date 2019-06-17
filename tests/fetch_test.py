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
        ac_fetch = AsyncURLFetch()
        ac_fetch.worker = 3
        self.assertEqual(ac_fetch.worker, 3)

    #def test_parallel_fetch_with_session(self):
    #    ac_fetch = AsyncURLFetch()
    #    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #    session = AsyncURLSession('GET' ,TEST_URL, headers=headers)
    #    ac_fetch.queue.put_nowait(session)
    #    print(ac_fetch.parallel().results)

if __name__ == '__main__':
    unittest.main()
