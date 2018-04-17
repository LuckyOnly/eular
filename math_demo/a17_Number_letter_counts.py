# coding:utf-8
import re
strings="one ,two  ,three , four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty"
L = re.split(r',|\s+',strings)
resource='ten,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'
S = resource.split(',')
token = {0:0,1:3}
cookie={10:3}
def ini2(L):
    i = 0
    j = 10
    while i < len(L):
        if j not in cookie:
            cookie[j] = len(L[i])
        i += 1
        j += 10
    return cookie

def ini1(L):
    i = 0
    j = 0
    while i < len(L):
        if len(L[i])!=0 :
            j+=1
            if j not in token:
                token[j] = len(L[i])
        i += 1
    return token

def count_letter(num):
    tmp = 0
    if 1 <= num <= 20:
        tmp =token[num]
        return tmp
    elif 20< num <100:
        c = num % 10
        b = num / 10
        tmp = cookie[b * 10] + token[c]
        return tmp
    elif 100<= num <=999:
        a = num / 100
        d=num % 100
        if  d== 0:
            tmp += token[a] + 7
            return tmp
        elif 0< d <=20:
            tmp += token[a] + 10 + token[d]
            return tmp
        else:
            b = num % 100 / 10
            c = num % 10
            tmp += token[a] + 10 +cookie[b * 10] + token[c]
            return tmp
    else:
            tmp = 11
            return tmp

#     # 计算值
def sum(num):
    i = 1
    tmp =0
    while i<=num:
        tmp+=count_letter(i)
        i+=1
    print tmp
ini1(L)
ini2(S)
sum(1000)
