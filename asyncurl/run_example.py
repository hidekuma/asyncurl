import AsyncURL

if __name__ == "__main__":
    urls = [
        'http://localhost',
        'http://localhost',
        'http://localhost',
        'http://localhost',
    ]

    asyncurl = AsyncURL.asyncurl()

    # case.1) with callback
    print('-------- [with callback] ----------')
    asyncurl.parallel_fetch(urls, callback=lambda x: print('with callback : {0}'.format(x)))
 
    # case.2) return results
    print('-------- [return results] ----------')
    print(asyncurl.parallel_fetch(urls).results)

    # case.3) print results for check
    print('-------- [print results] ----------')
    asyncurl.parallel_fetch(urls).print_results()
