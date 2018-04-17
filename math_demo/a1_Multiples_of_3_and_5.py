import logging
logging.basicConfig(level=logging.INFO,filename='mylog.log')

def sum(num):

    logging.info('input the number is :%d' % num )
    len1 = (num-1)/3
    len2 = (num-1)/5
    len3 = (num-1)/15
    i=1
    j=1
    k=1
    sum1=0
    sum2=0
    sum3=0
    while i <= len1:
        numbers = 3*i
        sum1 = sum1 +numbers
        i= i+1

    while j<=len2:
        numbers2 = 5*j
        sum2 = sum2 +numbers2
        j= j+1

    while k<=len3:
        numbers3 = 15*k
        sum3+=numbers3
        k+=1
    logging.info('the result is :%d' % (sum1+sum2-sum3))
    return sum1+sum2-sum3

print sum(1000)
