# coding:utf-8

token={}

i = 1
while True:
    num = i**3
    key = list(str(num))
    key.sort()
    key = ''.join(key)
    if token.get(key):
        token[key][0]+=1
        if token[key][0]==5:
            print token[key][1]
            break
    else:
        token[key]=[1,num]
    i +=1

