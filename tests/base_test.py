import unittest
import asyncio
from asyncurl.base import AsyncURLBase

class AsnyncURLBaseTest(unittest.TestCase):
    def test_instance(self):
        ac = AsyncURLBase()
        ac.worker = 3
        ac.limit = 1
        self.assertEqual(ac.worker, 3)

if __name__ == '__main__':
    unittest.main()
