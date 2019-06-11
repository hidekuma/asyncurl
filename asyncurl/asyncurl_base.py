import asyncio, uvloop

class AsyncURLBase:
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


