from asyncurl.fetch import AsyncURLFetch
from asyncurl.session import AsyncURLSession

TEST_URL = 'http://localhost'

ac_fetch = AsyncURLFetch()
urls = [TEST_URL]

for x in range(2):
    ac_fetch.queue.put_nowait(TEST_URL)

for x in range(2):
    session = AsyncURLSession()
    session.fetch_url = TEST_URL
    session.fetch_method = 'GET'
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    ac_fetch.queue.put_nowait(session)

#print(ac_fetch.parallel().results)
print(ac_fetch.parallel(urls, callback=lambda x:print(x)).results)
