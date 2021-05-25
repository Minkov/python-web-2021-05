from urllib import parse

tests = [
    ('http://www.google.bg/search?q=C%23', 'http://www.google.bg/search?q=C#'),
    ('https://mysite.com/show?n%40m3=p3%24h0', 'https://mysite.com/show?n@m3=p3$h0'),
    ('http://url-decoder.com/i%23de%25?id=23', 'http://url-decoder.com/i#de%?id=23'),
    ('http://url-decoder.com/name=Doncho%20Minkov', 'http://url-decoder.com/name=Doncho Minkov'),
]

for (test, expected) in tests:
    actual = parse.unquote(test)
    print(f'{expected == actual}: {expected}, {actual}')
