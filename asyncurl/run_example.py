import asyncurl

if __name__ == "__main__":
    urls = [
        'http://localhost',
        'http://localhost',
        'http://localhost',
        'http://localhost',
    ]

    asycurl = asyncurl.AsyncURL()

    # case.1) with callback
    print('-------- [with callback] ----------')
    asycurl.parallel_fetch(urls, callback=lambda x: print('with callback : {0}'.format(x)))
 
    # case.2) return results
    print('-------- [return results] ----------')
    print(asycurl.parallel_fetch(urls).results)

    # case.3) print results for check
    print('-------- [print results] ----------')
    asycurl.parallel_fetch(urls).print_results()
