# coding:utf-8
from collections import Counter
hands = map(int,open('./file/p059_cipher.txt').read().split(','))

key= [Counter(hands[i::3]).most_common(1)[0][0]^32 for i in range(3)]

print 'key is=',("").join(map(chr,key))
print len(hands)*1.0//3,len(key*(len(hands)//3+1))
print 'sum is =',sum(x^y for x,y in zip(hands,key*(len(hands)//3+1)))

# print zip([1,2,3],'abcd')












