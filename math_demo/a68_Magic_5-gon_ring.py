# coding:utf-8
L = [1, 2, 3, 4, 5,1, 2, 3, 4, 5]
def count(n):
    i = 0
    size = len(L)
    while i<len(L)-1:
        p = L[i]
        j = 1
        while j <=len(L)-1:
            q = L[j]
            if p+q+n == 14 and p!=q:
                yield n,p,q
                L.remove(p)
                L.remove(q)
                break
            j+=1
        if size == len(L)+2:
            break
        i+=1


def result():
    for i in xrange(6,11):
        for t in count(i):
            print t

# result()
print 6357528249411013<6531031914842725


