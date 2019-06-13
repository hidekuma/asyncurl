import unittest
from asyncurl.session import AsyncURLSession

TEST_URL ='http://github.com'

class AsyncURLSessionTest(unittest.TestCase):
    def test_instance_1(self):
        session = AsyncURLSession()
        session.fetch_url = TEST_URL
        self.assertEqual(session.fetch_url, TEST_URL)

    def test_instance_2(self):
        session = AsyncURLSession()
        session.fetch_method = 'POST' 
        self.assertEqual(session.fetch_method, 'POST')

if __name__ == '__main__':
    unittest.main()
