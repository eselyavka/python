#!/usr/bin/env python2.7

def lre(_str):
    if not _str:
        return ''

    if len(_str) == 1:
        return _str

    _prev, res = None, ''
    cnt = 1

    for i, c in enumerate(_str):
        if c == _prev:
            cnt += 1
        else:
            res += (_prev if _prev else '') + (str(cnt) if cnt > 1 else '')
            cnt = 1

        if i == len(_str) - 1:
            res += c + (str(cnt) if cnt > 1 else '')

        _prev = c

    return res

def main():
    payload = 'aaaabbcdrtty'
    assert lre(payload) == 'a4b2cdrt2y'

    payload = 'aaaabbcdrttyy'
    assert lre(payload) == 'a4b2cdrt2y2'

    payload = 'aa'
    assert lre(payload) == 'a2'

    payload = 'abcd'
    assert lre(payload) == 'abcd'

if __name__ == '__main__':
    main()
