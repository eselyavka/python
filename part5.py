#!/usr/bin/env python2.7
"""
Exercises from partVI Learning Python, Fifth Edition by Mark Lutz
"""

import unittest
import copy

class Adder(object):
    def __init__(self, data=None):
        self.data = data

    def __add__(self, other):
        return self.add(self.data, other)

    def add(self, x, y):
        raise NotImplementedError

class ListAdder(Adder):
    def add(self, x, y):
        if all([isinstance(x, list), isinstance(y, list)]):
            return x+y

class DictAdder(Adder):
    def add(self, x, y):
        if all([isinstance(x, dict), isinstance(y, dict)]):
            x.update(y)
            return x

class MyList(list):
    def __init__(self, data=None):
        self.data = copy.deepcopy(data) if data else []

    def __add__(self, other):
        if all([any([isinstance(self.data, list), isinstance(self.data, MyList)]),
                any([isinstance(other, list), isinstance(other, MyList)])]):
            return self.data + other

    def __mul__(self, times):
        return self.data * times

    def __getitem__(self, offset):
        return self.data[offset]

    def __len__(self):
        return len(self.data)

    def __getslice__(self, start, end):
        return self.data[start:end]

    def append(self, element):
        return self.data.append(element)

    def __getattr__(self, name):
        return getattr(self.data, name)

class MyListSub(MyList):
    _counter = 0

    def __init__(self, *args, **kwargs):
        self.adds = 0
        MyList.__init__(self, *args, **kwargs)

    def __add__(self, other):
        print 'call to __add__'
        self.adds += 1
        MyListSub._counter += 1
        return MyList.__add__(self, other)

    def _get_counters(self):
        return (self._counter, self.adds)

class Attrs(object):

    def __getattr__(self, name):
        print 'fetching attribute {0}'.format(name)
        return self.__dict__[name] if self.__dict__.has_key(name) else None

    def __setattr__(self, name, value):
        print 'set attribute {0} with value {1}'.format(name, value)
        self.__dict__[name] = value

def nested_traversals(struct, payload):
    if any([isinstance(struct, stype) for stype in [list, dict, set]]):
        for element in struct:
            nested_traversals(element, payload)
    else:
        payload.add(struct)

class MySet(set):

    def __init__(self, *args):
        self._payload = set()
        self._union = set()
        for arg in args:
            nested_traversals(arg, self._payload)
        set.__init__(self, self._payload)

    def union(self, *args):
        for arg in args:
            nested_traversals(arg, self._union)
        return set(self._union)

    def intersect(self, *args):
        next_set=set()
        previous_set=set()
        result=list()
        for arg in args:
            nested_traversals(arg, next_set)
            result.append(next_set & previous_set)
            previous_set=next_set
        return set(result)

class Lunch(object):
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)

    def result(self):
        return self.customer.getFood()

class Customer(object):
    def __init__(self):
        self.my_food = None

    def placeOrder(self, foodName, employee):
        self.my_food = employee.takeFood(foodName)

    def getFood(self):
        return self.my_food.name

class Employee(object):
    def takeFood(self, foodName):
        return Food(foodName)

class Food(object):
    def __init__(self, name):
        self.name = name

class TestAssigment(unittest.TestCase):
    def setUp(self):
        self.listAdder = ListAdder()
        self.dictAdder = DictAdder()
        self.myList = MyList([10, 5])
        self.mySubList = MyListSub([1, 2, 3])
        self.mySubList2 = MyListSub([34, 65, 73])
        self.my_attrs = Attrs()

    def test_list_adder(self):
        self.assertIsNone(self.listAdder.add([1, 2, 3], 'aaa'))
        self.assertIsNone(self.listAdder.add([1, 2, 3], 1))
        self.assertEqual(self.listAdder.add([1, 2, 3], [4]), [1, 2, 3, 4])
        self.assertIsNone(ListAdder(10) + [1, 2, 3])
        self.assertEqual(ListAdder([4]) + [1, 2, 3], [4, 1, 2, 3])

    def test_list_dict(self):
        self.assertIsNone(self.dictAdder.add({'key1':1, 'key2':2, 'key3':3}, 'aaa'))
        self.assertIsNone(self.dictAdder.add({'key1':1, 'key2':2, 'key3':3}, 1))
        self.assertEqual(self.dictAdder.add({'key1':1, 'key2':2, 'key3':3}, {'key':4}),
                         {'key1':1, 'key2':2, 'key3':3, 'key':4})
        self.assertIsNone(DictAdder(10) + {'key1':1, 'key2':2, 'key3':3})
        self.assertEqual(DictAdder({'key':4}) + {'key1':1, 'key2':2, 'key3':3},
                         {'key1':1, 'key2':2, 'key3':3, 'key':4})

    def test_my_list(self):
        self.assertIsNone(MyList(10) + [1, 2, 3])
        self.assertIsNone(MyList([10, 9, 8]) + 1)
        self.assertEqual(MyList([1, 2, 3]) + [4], [1, 2, 3, 4])
        self.assertEqual(MyList() + [9], [9])
        self.assertEqual(MyList([10, 'data'])[1], 'data')
        self.assertEqual(MyList([10, 'data']) * 3, [10, 'data', 10, 'data', 10, 'data'])
        self.assertEqual(len(MyList([9, 2, 3])), 3)
        self.assertEqual(MyList([9, 2, 3])[1:], [2, 3])
        self.assertEqual(MyList([9, 2, 3])[::-1], [3, 2, 9])
        self.myList.append(3)
        self.assertEqual(self.myList[:], [10, 5, 3])

    def test_my_list_sub(self):
        [self.mySubList + [element] for element in range(10)]
        self.assertEqual(self.mySubList._get_counters(), (10, 10))
        [self.mySubList2 + [element] for element in range(20)]
        self.assertEqual(self.mySubList2._get_counters(), (30, 20))

    def test_attrs(self):
        self.my_attrs.name = 'test'
        self.assertEqual(getattr(self.my_attrs, 'name'), 'test')
        self.assertIsNone(getattr(self.my_attrs, 'inexistent'))

    def test_my_set(self):
        self.assertEqual(MySet(1,2,3,['ddd',1,'www'], 'mmm'), set([1,2,3,'ddd','www','mmm']))
        result = MySet(1,2,3) & MySet(4,1) & MySet(1,50)
        self.assertEqual(result, set([1]))
        self.assertEqual(MySet(1).union(MySet([2,3,'ddd', 1, 'www']), MySet('mmm')), set([1,2,3,'ddd','www','mmm']))

    def test_composition(self):
        x = Lunch()
        x.order('burritos')
        self.assertEqual(x.result(), 'burritos')
        x.order('pizza')
        self.assertEqual(x.result(), 'pizza')

if __name__ == '__main__':
    unittest.main()
