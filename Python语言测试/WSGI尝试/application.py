def application(environ, start_response):
    print(environ)
    print(start_response)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<h1>Hello, web!</h1>'.encode()]