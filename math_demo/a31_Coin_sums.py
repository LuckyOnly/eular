# coding:utf-8
token={}
def coin_num():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0] * target

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
        print ways

    print "Ways to make change =", ways[target],len(ways)
def result():
    count = 1
    a = 200
    for m in range(0,a/100+1):
        for k in range(0,a/50+1):
            for l in range(0,a/20+1):
                for i in range(0,a/10+1):
                    for j in range(0,a/5+1):
                        for p in range(0,a/2+1):
                            for q in range(0,a/1+1):

                                if a == m*100+k*50+l*20+i*10+j*5+p*2+q*1:
                                    token[count]=[m,k,l,i,j,p,q]
                                    print token[count]
                                    count +=1
    return count

coin_num()