import unittest
from asyncurl.asyncurl_base import AsyncURLBase

class AsnyncURLBaseTest(unittest.TestCase):
    def test_instance(self):
        ac = AsyncURLBase()
        ac.worker = 3
        self.assertEqual(ac.worker, 3)

if __name__ == '__main__':
    unittest.main()
