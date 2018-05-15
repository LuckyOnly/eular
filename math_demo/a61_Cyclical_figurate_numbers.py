# coding:utf-8
import math
def triangle_method(n,idx):
    if idx == 3: t= val_method(1,1,-2*n)
    elif idx == 4: t=val_method(1,0,-n)
    elif idx == 5: t=val_method(3,-1,-2*n)
    elif idx == 6: t=val_method(2,-1,-n)
    elif idx == 7: t=val_method(5,-3,-2*n)
    return t == int(t)

def val_method(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/2*a

def figure(num,flag,idx):
    flag[idx] = num
    if flag.count(0)==0 and num % 100 == (flag[5]//100):
        print flag,sum(flag)
        return
    for mowei in range(10,100):
        nn = num % 100 *100+mowei
        for i in range(7,2,-1):
            if flag[i-3] ==0 and triangle_method(nn,i):
                figure(nn,flag,i-3)
                flag[i-3]=0


for i in range(21,22):
    Oct = i*(3*i -2)
    if Oct % 100>=10:
        figure(Oct,[0,0,0,0,0,0],5)

# print triangle_method(8128,3)
# print triangle_method(8281,4)
# print triangle_method(2882,5)