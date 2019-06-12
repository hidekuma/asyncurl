from asyncurl.fetch import AsyncURLFetch

TEST_URL = 'http://localhost'

ac_fetch = AsyncURLFetch()

for x in range(10):
    ac_fetch.queue.put_nowait(TEST_URL)

urls_generator = (TEST_URL for x in range(10))
urls = [
    TEST_URL,
    TEST_URL,
    TEST_URL,
    TEST_URL,
    TEST_URL,
    TEST_URL,
    TEST_URL,
]

print(ac_fetch.parallel().results)
#print(ac_fetch.parallel(urls, callback=lambda x:print(x)).results)
