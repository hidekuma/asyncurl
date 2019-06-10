import asyncio, requests, uvloop
import collections

#from collections.abc import AsyncIterator
#class CoreIter(AsyncIterator):
#    def __init__(self, urls):
#        self.urls = iter(urls)
#        self.__loop = None
#
#    def __aiter__(self):
#        self.__loop = asyncio.get_event_loop()
#        return self
#
#    async def __anext__(self):
#        try:
#            url = next(self.urls)
#            future = self.__loop.run_in_executor(None, requests.get, url)
#            resp = await future
#        except StopIteration:
#            raise StopAsyncIteration
#        return resp
#
#class FetchCore(CoreIter):
#    def __init__(self):
#        self.futures = []
#
#    async def async_fetch(self, urls):
#        aurl = CoreIter(urls)
#        async for resp in aurl:
#            print(type(resp), resp.url)
#            self.futures.append(resp)
#def fetch(urls):
#    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
#
#    fetch = FetchCore()
#
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(fetch.async_fetch(urls))
#
#    print('---')
#    print(fetch.futures)


class AsyncURL:
    def __init__(self):
        self._worker = 2
        self._results = []
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    @property
    def worker(self):
        return self._worker

    @worker.setter
    def worker(self, worker):
        if worker <= 0:
            raise ValueError("%f workers must be > 0." % worker)
        self._worker = worker

    @property
    def results(self):
        """
        - results get only.
        """
        if not self._results:
            raise ValueError('Result is empty now.')
        return self._results

    @staticmethod
    def help():
        print("""
        - nothing..
        """)

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
        - default callback()
        """
        self._results.append(future.result())

    def parallel_fetch(self, urls, *, callback=None):
        """
        - the order of result is nonsequential
        """
        if not isinstance(urls, list) and not isinstance(urls, collections.Generator):
            raise ValueError('can accept args like List or Generator.')

        # reset results
        self._results.clear()
        loop = asyncio.get_event_loop()

        if callback is None:
            callback = self._store_result

        loop.run_until_complete(self._queue_execution(urls, callback=callback))
        return self

    def print_results(self):
        """
        - for check results
        """
        if self._results:
            for r in self._results:
                print("print_result: {0}".format(r.url))
        else:
            raise ValueError('Result is empty now.')
