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
    assert parse_d('http://wordld_of_tanks.com/?premium=true&days=90') == {'premium': 'true', 'days': '90'}
    assert parse_d('http://google.com/catalog/?women=true&shoes=crocs&size=14.5') == {'women': 'true', 'shoes': 'crocs', 'size': '14.5'}
    assert parse_d('http://site.ru/index.php?name=Катя&surname=Иванова') == {'name': 'Катя', 'surname': 'Иванова' }
    assert parse_d('http://getrequest.com/index.php?thing=Стул&section=Мебель') == {'thing': 'Стул', 'section': 'Мебель'}
    assert parse_d('http://youtube.com/?video=true&size=120') == {'video': 'true', 'size': '120'}
    assert parse_d('http://staff.ua/?clothes=all&size=32=55&trousers=jeans&') == {'clothes': 'all', 'size': '32=55', 'trousers': 'jeans'}
    assert parse_d('http://amazon.com/?section=chairs') == {'section': 'chairs'}
    assert parse_d('http://population.ru/?mans=46%&womens=54%') == {'mans': '46%', 'womens': '54%'}
    assert parse_d('http://google.com/') == {}
    assert parse_d('http://account.org/?user=Stas&sec_name=Pop') == {'user': 'Stas', 'sec_name': 'Pop'}


#def parse_cookie(query: str) -> dict:
   # return {}


#if __name__ == '__main__':
    #assert parse_cookie('name=Dima;') == {'name': 'Dima'}
   # assert parse_cookie('') == {}
    #assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
   #assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}