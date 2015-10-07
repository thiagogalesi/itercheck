from six.moves import zip_longest
import itertools

def _any(seq, pred=None):
    """Returns True if an element of the list obeys the predicate
       If the predicate is None, works as builtin any"""
    if not pred:
        return any(seq)
    results = [k for k in seq if pred(k)]
    return bool(results)

def _all(seq, pred=None):
    """Returns True if all elements of the list obey the predicate
       If the predicate is None, works as builtin all"""
    if not pred:
        return all(seq)
    results = [pred(k) for k in seq]
    return all(results)

def all_same(seq, key=None):
    """Returns True if all elements of the list are equal
       (using key as the comparison value)
       If the key is None, uses simple equality"""
    if not key:
        key = lambda x:x
    first_elem = None
    is_first = True
    for ii in seq:
        i = key(ii)
        if is_first:
            first_elem = i
            is_first = False
            continue
        if i != first_elem:
            return False
    return True

def match_all(seq, f_seq, pred):
    """In a sequence, make sure all elements that match
       the predicate f_seq, match the predicate pred"""
    f_seq = [k for k in seq if f_seq(k)]
    return _all(f_seq, pred)

def match_any(seq, f_seq, pred):
    """In a sequence, make sure one element that matches
       the predicate f_seq, match the predicate pred"""
    f_seq = [k for k in seq if f_seq(k)]
    return _any(f_seq, pred)

def match_pair_any(seq1, seq2, pred):
    """Verify that there's a pair (seq1, seq2) that matches the predicate
       pred"""
    for k in itertools.product(seq1, seq2):
        if pred(k[0],k[1]):
            return True
    return False

def match_pair_all(seq1, seq2, pred, key=None, reverse=False):
    """Verify that all pairs (seq1, seq2), taken in order from the sequences
       (sorted optionally with key as in sort)
       match the predicate pred
       If one list is longer than the other, elements from the shorter
       sequence will be taken as None
       """
    sorted_seq1 = sorted(seq1, key=key, reverse=reverse)
    sorted_seq2 = sorted(seq2, key=key, reverse=reverse)
    result = True
    for k in zip_longest(sorted_seq1, sorted_seq2):
        if not pred(k[0],k[1]):
            result = False
    return result
