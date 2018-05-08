# coding:utf-8
def contructor_l(num):
    L=[]
    for i in range(1,num*num+1):
        L.append(i)
    return L


from prime_distinct import is_prime
token= {1:0,7:8,45: 28,91: 48,191:88,591:199,691:223,1001:300,1501:432,3501:913,3801:979,3901:1004,3961:1014,5001:1250,10001:2250}
def spiral_method(num):
    s = num
    if s in token:
        return token[s]
    token[s] = spiral_method(s-2)+splice_method(s)
    return token[s]



def splice_method(num):
    L = contructor_l(num)
    count = 0
    t = num*num -1
    p = num-1
    a = L[t:t-3*p-1:-p]
    # print a
    for i in a:
        if m_r(i):
            count += 1
    return count
def splice(num):
    L = contructor_l(num)
    size = len(L)
    d=1
    k= 3
    end = L[0]
    count = 0
    while end != L[size-1]:
        p= 2*d
        t= k*k-1
        a = L[t:t-3*p-1:-p]
        for i in a:
            if is_prime(i):
                count += 1
        d+=1
        k+=2
        end = a[0]
    print count
    return count*1.0/(2*num-1)

def count_num():
    i = 10001
    while i:
        print i,spiral_method(i),spiral_method(i)*1.0/(2*i-1)
        if spiral_method(i)*1.0/(2*i-1)<=0.1:
            return i
        i+=2

from Euler import miller_rabin as m_r


def euler_method():
    d, n, n_prime, avg = 1, 2, 0, 1
    while avg >= 0.1:
        n_prime += m_r(d + n) + m_r(d + 2 * n) + m_r(d + 3 * n)
        avg = n_prime*1.0 / (2 * n + 1)
        d += 4 * n
        n += 2

    return n-1
# print count_num()
print euler_method()
# print splice(20001)