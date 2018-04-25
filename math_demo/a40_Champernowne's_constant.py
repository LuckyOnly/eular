# coding:utf-8


def conctruct_data():
    strings = ""
    j=0
    sum=1
    i = 1
    while True:
        strings+=str(i)
        if len(strings)>=1000000:
            break
        i+=1
    while j<=6:
        sum*=int(strings[10**j-1])
        j+=1
    return sum

print conctruct_data()