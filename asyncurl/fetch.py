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
                session = AsyncURLSession()

            future = loop.run_in_executor(None, session.send)

            if callback:
                future.add_done_callback(callback)
            else:
                future.add_done_callback(self._store_result)
            await future
            session.close()

    async def _queue_execution(self, *, callback):
        """
        - call by parallel_fetch()
        """
        loop = asyncio.get_event_loop()

        #if arg_urls:
        #    for url in arg_urls:
        #        self.queue.put_nowait(url)

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

    def parallel(self, *, callback=None):
        """
        - [ENTRYPOINT]
        - validation
        - the order of result is nonsequential
        """
        #self._validate(urls)
        self._results.clear() # RESET results

        loop = asyncio.get_event_loop()

        loop.run_until_complete(self._queue_execution(callback=callback))

        return self
