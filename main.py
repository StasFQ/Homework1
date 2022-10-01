def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(cooks) -> dict:
    if cooks:
        cooks = cooks.split(';')
        if '' in cooks:
            cooks.remove('')
        d = dict(h.split('=', 1) for h in cooks)
        return d
    if cooks == '':
        return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('job=dantist=worker=zubnik;salary=2300$') == {'job': 'dantist=worker=zubnik', 'salary': '2300$'}
    assert parse_cookie('category=women;user=Lilia;password=1234;position=teacher') == {'category': 'women', 'user': 'Lilia', 'password': '1234', 'position': 'teacher'}
    assert parse_cookie('title=king=prince;wars=2;name=Alexandr') == {'title': 'king=prince', 'wars': '2', 'name': 'Alexandr'}
    assert parse_cookie('city=Odessa;region=Moldovanka;flat=45;') == {'city': 'Odessa', 'region': 'Moldovanka', 'flat': '45'}
    assert parse_cookie('population=134000;women=43%;mans=57%') == {'population': '134000', 'women': '43%', 'mans': '57%'}
    assert parse_cookie('children=4;sons=3;girls=1') == {'children': '4', 'sons': '3', 'girls': '1'}
    assert parse_cookie('fruit=apple=banana=orange;count=12') == {'fruit': 'apple=banana=orange', 'count': '12'}
    assert parse_cookie('school=2;classrooms=54;students=890') == {'school': '2', 'classrooms': '54', 'students': '890'}
    assert parse_cookie('cars=3;mazda=1;mercedes=1;bmw=1;') == {'cars': '3', 'mazda': '1', 'mercedes': '1', 'bmw': '1'}
    assert parse_cookie('names=3;') == {'names': '3'}
