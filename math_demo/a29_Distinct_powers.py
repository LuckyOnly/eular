# coding:utf-8
token={}
def distinct_num(value):
    if value in token:
        return False
    return True


def every_item(num):
    count = 0
    for i in range(2,num+1):
        for j in range(2,num+1):
            value = i**j
            if distinct_num(value):
                token[value]=[i,j]
                count +=1
    return count

print every_item(100)