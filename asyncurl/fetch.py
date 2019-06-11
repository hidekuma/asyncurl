import collections
import requests
from asyncurl.base import AsyncURLBase, asyncio, uvloop

class AsyncURLFetch(AsyncURLBase):
    def __init__(self):
        super().__init__()

    async def _queue_fetch(self, loop, queue, callback):
        """
        - call by _queue_execution()
        """
        while not queue.empty():
            url = await queue.get()
            future = loop.run_in_executor(None, requests.get, url)
            if callback is not None:
                future.add_done_callback(callback)
            await future

    async def _queue_execution(self, arg_urls, *, callback):
        """
        - call by parallel_fetch()
        """
        loop = asyncio.get_event_loop()
        queue = asyncio.Queue()

        for url in arg_urls:
            queue.put_nowait(url)

        tasks = [self._queue_fetch(loop, queue, callback) for i in range(self._worker)]
        return await asyncio.wait(tasks)

    def _store_result(self, future):
        """
        - default callback
        """
        self._results.append(future.result())

    def parallel(self, urls, *, callback=None):
        """
        - the order of result is nonsequential
        """
        if not isinstance(urls, collections.Iterable):
            raise ValueError('can accept args like Iterable')

        # reset results
        self._results.clear()
        loop = asyncio.get_event_loop()

        if callback is None:
            callback = self._store_result

        loop.run_until_complete(self._queue_execution(urls, callback=callback))
        return self
