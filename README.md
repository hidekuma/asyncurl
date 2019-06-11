# asyncurl
Asynchronous cURL Requests

<img src="https://raw.githubusercontent.com/hidden-function/i/master/asyncurl.png" height="500" alt="asyncurl-logo"> 

---
## Dependencies
| Package  | Version  | Description |
| :-:      | :-:      | :-:         |
| python   | >=3.6    |             |
| asyncio  | >=3.4.3  |             |
| requests | >=2.22.0 |             |
| uvloop   | >=0.12.2 |             |

## Installation
asyncurl project consists of the following packages:
- `asyncio`
- `requests` (not `pycurl`)
- `uvloop`

You can [download asyncurl executable](https://github.com/hidden-function/asyncurl/releases).

### Using pip
```bash
pip install asyncurl
```

## Usage
if you want asyncurl, you have to import like this.
```python
from asyncurl import asyncurl

ac = asyncurl.AsyncURL()
```

Default worker's count is 2. you can change it if you want.
```python
ac.worker = 3
```

and you can fetch urls.
```python
urls = [
  "http://localhost",
  "http://localhost",
  "http://localhost"
]
ac.parallel_fetch(urls)
```
`parallel_fetch` function which can return list of request class. just like this.
```python
ac.parallel_fetch(urls).results
```
The function's the order of result is nonsequential

## Examples
```python
# case.1) with callback
print('-------- [with callback] ----------')
asycurl.parallel_fetch(urls, callback=lambda x: print('with callback : {0}'.format(x)))

# case.2) return results
print('-------- [return results] ----------')
print(asycurl.parallel_fetch(urls).results)

# case.3) print results for check
print('-------- [print results] ----------')
asycurl.parallel_fetch(urls).print_results()

>>>
-------- [with callback] ----------
with callback : <Future finished result=<Response [403]>>
with callback : <Future finished result=<Response [403]>>
with callback : <Future finished result=<Response [403]>>
with callback : <Future finished result=<Response [403]>>
-------- [return results] ----------
[<Response [403]>, <Response [403]>, <Response [403]>, <Response [403]>]
-------- [print results] ----------
print_result: http://localhost/
print_result: http://localhost/
print_result: http://localhost/
print_result: http://localhost/
```

[License](LICENSE)
------------------

The MIT License (MIT)

Copyright (c) 2019 Hidden function by hidekuma
