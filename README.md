# asyncurl [![Build Status](https://travis-ci.org/hidden-function/asyncurl.svg?branch=master)](https://travis-ci.org/hidden-function/asyncurl)
for Asynchronous cURL Requests using python, which is inspired by this benchmark([KR](https://hidekuma.github.io/python/uvloop/), [EN](https://magic.io/blog/uvloop-blazing-fast-python-networking/))

<img src="https://raw.githubusercontent.com/hidden-function/i/master/asyncurl.png" width="50%" alt="asyncurl-logo"> 

---
## Support python versions
python >= 3.6

## Dependencies
AsyncURL project consists of the following packages:

| Package  | Version  | Description           |
| :-:      | :-:      | :-:                   |
| asyncio  | >=3.4.3  | for Asynchronous      |
| requests | >=2.22.0 | pycurl substitutes    |
| uvloop   | >=0.12.2 | for event loop policy |

## Installation
You can [download asyncurl executable](https://github.com/hidden-function/asyncurl/releases) and [binary distributions from PyPI](https://pypi.org/project/asyncurl/).

### Using pip
```bash
pip install asyncurl
```

## Usage
How to import AsnycURL:
```python
from asyncurl.fetch import AsyncURLFetch

ac_fetch = AsyncURLFetch()
```

Default worker's count is 2. you can change it if you want.
```python
ac_fetch.worker = 3
```

and you can put urls to `<AsyncURl.queue>`.
```python
for x in range(2):
    ac_fetch.queue.put_nowait('http://localhost')

ac_fetch.parallel()
```
then call `parallel()`. The fucntion fetch urls using `<requests>`(the only Non-GMO HTTP library for Python).

and AsyncURL can change `<requests>`'s method and else properties.
```python
from asyncurl.session import AsyncURLSession
from asyncurl.fetch import AsyncURLFetch

ac_fetch = AsyncURLFetch()

for x in range(2):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    session = AsyncURLSession('GET', 'http://localhost', headers=headers)
    ac_fetch.queue.put_nowait(session)
    ac_fetch.queue.put_nowait(session)

ac_fetch.parallel()
```
`AsyncURLSession` is inheritance of `<requests.Session>`.

`parallel()` will return `<AsncURLFetch>`, and it can show results to you.

### else properties
- params=None
- data=None
- headers=None
- cookies=None
- files=None
- auth=None
- timeout=None
- allow_redirects=True
- proxies=None
- hooks=None
- stream=None
- verify=None
- cert=None
- json=None

Show results:
```python
ac_fetch.parallel().results
```
The order of result is nonsequential. and it will return list of `<requests.Response>`.

## Examples
```python
# case.1) with callback
print('[with callback]')
ac_fetch.parallel(callback=lambda x: print('with callback : {0}'.format(x)))

# case.2) return results
print('[return results]')
print(ac_fetch.parallel().results)

>>>
[with callback]
with callback : <Future finished result=<Response [403]>>
with callback : <Future finished result=<Response [403]>>
with callback : <Future finished result=<Response [403]>>

[return results]
[<Response [403]>, <Response [403]>, <Response [403]>]
```

[License](LICENSE)
------------------

The MIT License (MIT)

Copyright (c) 2019 Hidden function by hidekuma
