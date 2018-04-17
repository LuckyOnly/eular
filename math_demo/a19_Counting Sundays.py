# coding:utf-8

def is_leap(num):
    if num % 100==0 and num%400==0:
        return True
    if  num % 100!= 0 and num%4==0:
        return True
    return False

def days(num,date):
    if date == 2:
        if is_leap(num):
            sum = cookie[date][1]
        else:
            sum = cookie[date][0]
    else:
        sum = cookie[date]
    return sum

token ={1:'Monday',2:'Tuesday',3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
cookie ={1:31}
def mouth_days():
    i=1
    while i <=12:
        if i not in cookie:
            if  i in [9,4,6,11]:
                cookie[i]=30
            elif i in [2]:
                cookie[i] = [28,29]
            else:
                cookie[i]=31
        i+=1
    return cookie
def suns():
    count = 2
    sum = 0
    num = 1901
    while num <= 2000:
        print "year:" + str(num)
        print "count:" + token[count]
        i = 1
        while i<=12:
            count=(days(num,i)%7+count)%7
            if count == 0:
                sum+=1
                count = 7
            i+=1
        num+=1
    return sum

print mouth_days()
print suns()
# print days(2004,2)
# print days(2004,1)