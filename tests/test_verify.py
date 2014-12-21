import nose.tools as nt
from itercheck import verify

def test_all():
    nt.assert_true(verify._all([1, 2, 3]))
    nt.assert_true(verify._all([1, 3, 5], lambda x:(x%2)))

def test_any():
    nt.assert_true(verify._any([0, 2, 0]))
    nt.assert_false(verify._any([0, 0, 0]))
    nt.assert_true(verify._any([1, 2, 3], lambda x:x%2 - 1))
    nt.assert_false(verify._any([4, 2, 6], lambda x:x%2))

def test_all_same():
    nt.assert_true(verify.all_same([]))
    nt.assert_true(verify.all_same([2, 2, 2, 2]))
    nt.assert_false(verify.all_same([1, 2, 3]))
    nt.assert_false(verify.all_same(range(5)))
    nt.assert_true(verify.all_same(range(5),lambda x:(x<10)))
    nt.assert_false(verify.all_same(range(50),lambda x:(x<10)))

def test_match_all():
    nt.assert_true(verify.match_all(range(10), lambda x:not x%2, lambda x: (x<9)))
    nt.assert_false(verify.match_all(range(10), lambda x:x%2, lambda x: (x<5)))

def test_match_pair_any():
    nt.assert_true(verify.match_pair_any(range(10, 20, 2), range(10, 20, 3), lambda a, b:a==b))
    nt.assert_false(verify.match_pair_any(range(10, 20, 5), range(10, 20, 3), lambda a, b:(a==b and a != 10)))

def test_match_pair_all():
    nt.assert_true(verify.match_pair_all([2, 3, 1], [1, 2, 3], lambda a, b:a==b))
    nt.assert_true(verify.match_pair_all([2, 3, 1], [1, 2, 3, 4], lambda a, b:a==b if (a and b) else True))
    nt.assert_true(verify.match_pair_all(range(10, 20, 2), range(10, 20, 2), lambda a, b:a==b))
