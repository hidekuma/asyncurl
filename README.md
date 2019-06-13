# asyncurl [![Build Status](https://travis-ci.org/hidden-function/asyncurl.svg?branch=master)](https://travis-ci.org/hidden-function/asyncurl)
Asynchronous cURL Requests

<img src="https://raw.githubusercontent.com/hidden-function/i/master/asyncurl.png" width="50%" alt="asyncurl-logo"> 

---
## Support python versions
python >= 3.6

## Dependencies
asyncurl project consists of the following packages:

| Package  | Version  | Description           |
| :-:      | :-:      | :-:                   |
| asyncio  | >=3.4.3  | Asynchronous          |
| requests | >=2.22.0 | pycurl substitutes    |
| uvloop   | >=0.12.2 | for event loop policy |

## Installation
You can [download asyncurl executable](https://github.com/hidden-function/asyncurl/releases).

### Using pip
```bash
pip install asyncurl
```

## Usage
if you want asyncurl, you have to import like this.

```python
from asyncurl.fetch import AsyncURLFetch

ac_fetch = AsyncURLFetch()
```

Default worker's count is 2. you can change it if you want.
```python
ac_fetch.worker = 3
```

and you can request urls.
```python
urls = [
  "http://localhost",
  "http://localhost",
  "http://localhost"
]
ac_fetch.parallel(urls)
```

List of url will be added to `asyncio.Queue`. so do like this if you want better performance.
```python
for x in range(2):
    ac_fetch.queue.put_nowait('http://localhost')

ac_fetch.parallel()
```

and AsyncURL can change request method and else.
```python
from asyncurl.session import AsyncURLSession
from asyncurl.fetch import AsyncURLFetch

ac_fetch = AsyncURLFetch()

for x in range(2):
    session = AsyncURLSession()
    session.fetch_url = 'http://localhost' 
    session.fetch_method = 'POST'
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    ac_fetch.queue.put_nowait(session)

ac_fetch.parallel()
```
`AsyncURLSession` is Inheritance of `<requests.Session>`.

`parallel` function will return itself. you can get results like this.
```python
ac_fetch.parallel(urls).results
```
The function's order of result is nonsequential. and it will return list of `<requests.Response>`.

## Examples
```python
# case.1) with callback
print('-------- [with callback] ----------')
ac_fetch.parallel(urls, callback=lambda x: print('with callback : {0}'.format(x)))

# case.2) return results
print('-------- [return results] ----------')
print(ac_fetch.parallel(urls).results)

>>>
>>> --- [with callback] ----------
>>> with callback : <Future finished result=<Response [403]>>
>>> with callback : <Future finished result=<Response [403]>>
>>> with callback : <Future finished result=<Response [403]>>
>>> 
>>> -------- [return results] ----------
>>> [<Response [403]>, <Response [403]>, <Response [403]>]
```

[License](LICENSE)
------------------

The MIT License (MIT)

Copyright (c) 2019 Hidden function by hidekuma
