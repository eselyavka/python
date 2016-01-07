#!/usr/bin/env python
"""
This is exercises from Learning Python Part IV
"""

def copy_dict(dict1):
    """Return new dictionary"""
    return {n:dict1[n] for n in dict1.keys()}

def add_dict(dict1, dict2):
    """Return new dictionary from all the items contained in both"""
    union_dict = dict()
    uniq_keys1 = set(dict1.keys())
    uniq_keys2 = set(dict2.keys())
    sunion = uniq_keys1 & uniq_keys2
    sdiff = uniq_keys1 ^ uniq_keys2

    for element in sunion:
        union_dict[element] = dict1[element]

    for element in sdiff:
        if dict1.has_key(element):
            union_dict[element] = dict1[element]

        if dict2.has_key(element):
            union_dict[element] = dict2[element]

    return union_dict

def adder(*vargs, **kargs):
    """Return sum/concatenate result from arbitrary number of arguments"""
    uniq_list_elements = set([type(x) for x in vargs])
    uniq_keys = set([type(x) for x in kargs.values()])

    if (len(uniq_list_elements) == 1 and
        len(uniq_keys) == 1 and
        len(uniq_list_elements ^ uniq_keys) == 0):
        summator = uniq_list_elements.pop()()
    else:
        print 'Should be the same type'

    for element in vargs:
        summator += element

    for element in kargs.values():
        summator += element

    return summator

def countdown(counter):
    """Self-recursive generator"""
    if counter == 0:
        yield 'stop'
    else:
        yield counter
        for element in countdown(counter-1):
            yield element

def main():
    """Command line entry point."""
    print adder('hello', 'world', 'bbbb', 'mmm', str1='sss', str2='nnnn')
    print adder([1, 2, 3], [4, 5, 6], [7, 8, 9], mas=[10, 50, 60])
    print adder(32.6, 89.2, float1=90.4)
    print copy_dict({'i':45, 'f':0.95, 'mas':[1, 6, 7]})
    print add_dict({'i':40, 'f':0.95, 'mas':[1, 6, 4]},
                  {'str':'bbb', 'i':90, 'd':{'b':1, 'c':3}})

    for element in countdown(5):
        print element

if __name__ == '__main__':
    main()
