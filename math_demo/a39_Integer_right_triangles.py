# coding:utf-8
def is_triangle(a,b,c):
    if a+b>c and a-b<c and b>=a:
        return True
    return False


import math
def count_method(p):
    count = 0
    for a in range(1,p/2):
        for b in range(a,p/2):
            for c in range(int(math.sqrt(a**2+b**2)),p/2):
                if a+b+c == p and is_triangle(a,b,c) and a**2+b**2==c**2:
                    # print a,b,c
                    count+=1
    return count


def method():
    max_num = 0
    tmp = 0
    for i in range(1001,3,-1):
        n = count_method(i)
        if n!=0:
            if n>max_num:
                max_num = n
                tmp = i
                print max_num,tmp
    return tmp



# {20,48,52}, {24,45,51}, {30,40,50}
# print is_triangle(20,48,52)
# print is_triangle(24,45,51)
# print is_triangle(30,40,50)
# print count_method(120)
print method()