import collections
from asyncurl.base import AsyncURLBase, asyncio, uvloop
from asyncurl.session import AsyncURLSession

class AsyncURLFetch(AsyncURLBase):
    def __init__(self):
        super().__init__()

    def __getattr__(self, name):
        return super().__getattr__(name)

    def _validate(self, urls):
        if not isinstance(urls, collections.Iterable):
            raise ValueError('urls arg can accept only Iterable')

    async def _queue_fetch(self, loop, callback):
        """
        - call by _queue_execution()
        """
        while not self.queue.empty():
            session = await self.queue.get()

            if not isinstance(session, AsyncURLSession):
                session = AsyncURLSession(fetch_url=session)

            if session.fetch_method == 'POST':
                future = loop.run_in_executor(None, session.post, session.fetch_url)
            elif session.fetch_method == 'PUT':
                future = loop.run_in_executor(None, session.put, session.fetch_url)
            elif session.fetch_method == 'DELETE':
                future = loop.run_in_executor(None, session.DELETE, session.fetch_url)
            else:
                future = loop.run_in_executor(None, session.get, session.fetch_url)

            if callback:
                future.add_done_callback(callback)
            else:
                future.add_done_callback(self._store_result)
            await future
            session.close()

    async def _queue_execution(self, arg_urls, *, callback):
        """
        - call by parallel_fetch()
        """
        loop = asyncio.get_event_loop()

        if arg_urls:
            for url in arg_urls:
                self.queue.put_nowait(url)

        tasks = [self._queue_fetch(loop, callback) for i in range(self._worker)]
        return await asyncio.wait(tasks)

    def _store_result(self, future):
        """
        - default callback
        """
        self._results.append(future.result())

    #async def _fetch(self, url, callback):
    #    r = requests.get(url)
    #    if callback:
    #        r = callback(r)
    #    return r

    #async def _execution(self, arg_urls, callback):
    #    reqs = [self._fetch(url, callback) for url in arg_urls]
    #    return await asyncio.wait(reqs)

    def parallel(self, urls=[], *, callback=None):
        """
        - [ENTRYPOINT]
        - validation
        - the order of result is nonsequential
        """
        self._validate(urls)
        self._results.clear() # RESET results

        loop = asyncio.get_event_loop()

        loop.run_until_complete(self._queue_execution(urls, callback=callback))

        return self
