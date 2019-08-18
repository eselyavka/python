#!/usr/bin/env python2.7

def lre(str_):
    if not str_:
        return ''

    if len(str_) == 1:
        return str_

    prev, res, cnt = None, '', 1

    for i, c in enumerate(str_):
        if c == prev:
            cnt += 1
        else:
            res += (prev if prev else '') + (str(cnt) if cnt > 1 else '')
            cnt = 1

        if i == len(str_) - 1:
            res += c + (str(cnt) if cnt > 1 else '')

        prev = c

    return res

def main():
    payload = None
    assert lre(payload) == ''

    payload = 'c'
    assert lre(payload) == 'c'

    payload = 'aaaabbcdrtty'
    assert lre(payload) == 'a4b2cdrt2y'

    payload = 'aaaabbcdrttyy'
    assert lre(payload) == 'a4b2cdrt2y2'

    payload = 'aa'
    assert lre(payload) == 'a2'

    payload = 'abcd'
    assert lre(payload) == 'abcd'

    payload = 'abcdddddd'
    assert lre(payload) == 'abcd6'

if __name__ == '__main__':
    main()
