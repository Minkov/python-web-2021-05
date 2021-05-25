def read_paths():
    END_COMMAND = 'END'

    paths = {
        'GET': [],
        'POST': [],
    }

    while True:
        the_input = input()
        if the_input == END_COMMAND:
            break
        path = the_input[:the_input.rindex('/')]
        method = the_input[the_input.rindex('/') + 1:]
        paths[method.upper()].append(path)
    return paths


def read_request():
    method, path, *_ = input().split(' ')
    return {
        'method': method,
        'path': path,
    }


def make_request(paths, request):
    valid_paths_for_method = paths[request['method']]

    if request['path'] in valid_paths_for_method:
        return '''HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain

OK'''
    else:
        return '''HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain

Not Found'''



def solve():
    paths = read_paths()
    request = read_request()
    result = make_request(paths, request)
    print(paths)
    print(request)
    print(result)


solve()
