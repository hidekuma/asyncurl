from asyncurl.fetch import AsyncURLFetch
from asyncurl.session import AsyncURLSession

TEST_URL = 'http://localhost'

ac_fetch = AsyncURLFetch()

for x in range(2):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    session = AsyncURLSession('GET' ,TEST_URL, headers=headers)
    ac_fetch.queue.put_nowait(session)

results = ac_fetch.parallel().results
for r in results:
    print(r.text)


# ac_fetch.parallel(callback=lambda x: print('with callback : {0}'.format(x)))
