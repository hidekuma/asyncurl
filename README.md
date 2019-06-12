# asyncurl <img src="https://api.travis-ci.org/hidden-function/asyncurl.svg?branch=master" alt="travis-ci-build-result"> 
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
List of url will be added to `asyncio.Queue`. so if you want better performance, do like this.
```python
for x in range(3):
    ac_fetch.queue.put_nowait('http://localhost')

ac_fetch.parallel()
```

`parallel` function will return itself. you can get results like this.
```python
ac_fetch.parallel(urls).results
```
The function's the order of result is nonsequential. and the results return that list of `<requests.Response>`.

## Examples
```python
# case.1) with callback
print('-------- [with callback] ----------')
ac_fetch.parallel(urls, callback=lambda x: print('with callback : {0}'.format(x)))

# case.2) return results
print('-------- [return results] ----------')
print(ac_fetch.parallel(urls).results)

>>>
-------- [with callback] ----------
with callback : <Future finished result=<Response [403]>>
with callback : <Future finished result=<Response [403]>>
with callback : <Future finished result=<Response [403]>>

-------- [return results] ----------
[<Response [403]>, <Response [403]>, <Response [403]>]
```

[License](LICENSE)
------------------

The MIT License (MIT)

Copyright (c) 2019 Hidden function by hidekuma
