# coding:utf-8

def Pythagorean():
    a=1
    while 0<a<500 :
        b= (500-a)*1000/(1000-a)
        c=1000-a-b
        if a*a+b*b==c*c:
            return a*b*c
        a+=1
print Pythagorean()