from urllib import parse
def parse_d(url) -> dict:
    if url:
        parse.urlsplit(url)
        parse.parse_qs(parse.urlsplit(url).query)
        a = dict(parse.parse_qsl(parse.urlsplit(url).query))
        return a
    else:
        return {}


if __name__ == '__main__':
    assert parse_d('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_d('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse_d('http://example.com/') == {}
    assert parse_d('http://example.com/?') == {}
    assert parse_d('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')
    assert parse_d('')


#def parse_cookie(query: str) -> dict:
   # return {}


#if __name__ == '__main__':
    #assert parse_cookie('name=Dima;') == {'name': 'Dima'}
   # assert parse_cookie('') == {}
    #assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
   #assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}