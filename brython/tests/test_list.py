# list examples

z = [1, 2, 3]
assert z.__class__ == list
assert isinstance(z, list)
assert str(z) == "[1, 2, 3]"

a = ['spam', 'eggs', 100, 1234]
assert a[:2] + ['bacon', 2 * 2] == ['spam', 'eggs', 'bacon', 4]
assert 3 * a[:3] + ['Boo!'] == ['spam', 'eggs', 100,
    'spam', 'eggs', 100,
    'spam', 'eggs', 100, 'Boo!']
assert a[:] == ['spam', 'eggs', 100, 1234]
a[2] = a[2] + 23
assert a == ['spam', 'eggs', 123, 1234]
a[0:2] = [1, 12]
assert a == [1, 12, 123, 1234]
a[0:2] = []
assert a == [123, 1234]
a[1:1] = ['bletch', 'xyzzy']
assert a == [123, 'bletch', 'xyzzy', 1234]
a[:0] = a
assert a == [123, 'bletch', 'xyzzy', 1234, 123, 'bletch', 'xyzzy', 1234]
a[:] = []
assert a == []
a.extend('ab')
assert a == ['a', 'b']
a.extend([1, 2, 33])
assert a == ['a', 'b', 1, 2, 33]

# tuple
t = (1,8)
assert t.__class__ == tuple
assert isinstance(t,tuple)
assert str(t)=='(1, 8)'

# bug reported on the mailing list
d = {}
d[ (1,3) ] = None
d[ (-1,3) ] = None
d[ (1,-3) ] = None
d[ (-1,-3) ] = None

assert d == { (1, 3): None,
    (-1, 3): None,
    (1, -3): None,
    (-1, -3): None
}

# list subclass - issue 893
class List(list):
      def __getitem__(self, item):
        return "TEST"
lst = List()
assert lst.__getitem__(100) == "TEST"
assert lst[100] == "TEST"

x = ['a','r','bg','Z']
x.sort()
assert x==['Z','a','bg','r']

x.sort(key=str.lower)
assert x==['a','bg','r','Z']

x.sort(key=str.lower,reverse=True)
assert x==['Z','r','bg','a']

x = ['a']
x.append('tail')
assert x == ['a','tail']
x.append([0,1])
assert x == ['a','tail',[0,1]]

assert x.count('a')==1
x.extend(['u','v'])

assert x==['a','tail',[0,1],'u','v']

assert x.index('u')==3

x.remove('tail')
assert x==['a',[0,1],'u','v']

x.pop()
assert x==['a',[0,1],'u']

x.pop(1)
assert x==['a','u']

x = ['a','r','bg','Z']
x.reverse()
assert x==['Z','bg','r','a']

del x[0]
assert x == ['bg','r','a']
del x[-1]
assert x == ['bg','r']

x += ['zz']
assert x == ['bg','r','zz']

assert x[1] == 'r'

assert 'r' in x
assert 'rty' not in x

# issue 364
class A(list):
    def __init__(self, x):
        list.__init__(self, x)

z = A([1,2,3])
assert isinstance(z, A)
assert z == [1, 2, 3]
assert len(z) == 3
assert list.__len__(z) == 3

z.foo = 5
assert z.foo == 5

# issue 724
t = [2]
try:
    t.foo = 8
    raise Exception("sould have raised AttributeError")
except AttributeError:
    pass

class List(list):

    counter = 0

    def pop(self, index=-1):
        return "POP"

    def reverse(self):
        return "REVERSE"

    def __setitem__(self, k, v):
        List.counter = 1

    def sort(self, key=None, reverse=False):
        return "SORT"

t = List([2, 1])
assert t.sort() == "SORT"
t2 = List()
List()[0] = 0
assert List.counter == 1
assert List().reverse() == "REVERSE"
assert List().pop() == "POP"

# issue 941
assert not [1] < [1]
assert [1] < [1, 2]
assert [0] < [1]
assert not [3] < [1, 2]

assert not ['a'] < ['a']
assert ['a'] < ['a', 2]

# issue 993
assert sorted(['b3', 'a2', 'c1']) == ['a2', 'b3', 'c1']
assert sorted(['a2', 'b3', 'c1'], key=lambda a:a[1]) == ['c1', 'a2', 'b3']
assert sorted(['a2', 'b3', 'c1'], key=None) == ['a2', 'b3', 'c1']

ls = ['b3', 'a2', 'c1']; ls.sort()
assert ls == ['a2', 'b3', 'c1']
ls = ['a2', 'b3', 'c1']; ls.sort(key=lambda a:a[1])
assert ls == ['c1', 'a2', 'b3']
ls = ['a2', 'b3', 'c1']; ls.sort(key=None)
assert ls == ['a2', 'b3', 'c1']

print("passed all tests..")