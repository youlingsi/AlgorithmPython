idLst = [0,1,9,4,9,6,6,7,8,9];
i = len(idLst);

"""Find the root of the given number"""
def findRoot(n):
    if n == idLst[n]:
        return n;
    elif n < i :
        m = idLst[n];
        return findRoot(m);
    else:
        return "error";

"""Merge the trees of the given number"""
def unionTree(p, q):
    rp = findRoot(p);
    rq = findRoot(q);
    if rp != rq:
        idLst[rq] = rp;

unionTree(3, 5);
print(findRoot(3), findRoot(5));
