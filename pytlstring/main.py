"""
Two-letter strings

There are two-letter strings, 'AA', 'AB' and 'BB', which appear AB, AB and BB
times respectevely. The task is to join some of these strings to create the
longest possible string which does not contain 'AAA' or 'BBB'.
"""

TLS = 'AA', 'AB', 'BB'

class _ltnode(object):
    def __init__(self, parent, lt):
        self.parent = parent
        self.lt = lt
        self.len = 1

        if parent is not None:
            self.len += parent.len

    def __len__(self):
        return self.len

    @classmethod
    def valid(cls, p, lt):
        if p is None:
            return True

        if p.lt[0] == p.lt[1] and p.lt[0] == lt[0]:
            return False

        if p.lt[1] == lt[0] and p.lt[1] == lt[1]:
            return False

        return True

    @classmethod
    def string(cls, l):
        s = []

        while l is not None:
            s.insert(0, l.lt)
            l = l.parent

        return s

def _ltnext(p, cc):
    ss = []

    for i, lt in enumerate(TLS):
        if cc[i] > 0 and _ltnode.valid(p, lt):
            cc1 = list(cc)
            cc1[i] -= 1
            ss.append(_ltnext(_ltnode(p, lt), cc1))

    if not len(ss):
        return p

    ll = [len(s) for s in ss]

    return ss[ll.index(max(ll))]

def tlstring(aa, ab, bb):
    """
    Return the longest two-letter string.
    """
    n = _ltnext(None, (aa, ab, bb))

    if n is None:
        return ""

    return "".join(n.string(n))
