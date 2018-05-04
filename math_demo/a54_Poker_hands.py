# coding:utf-8

from collections import Counter
hands = (line.split() for line in open('./file/p054_poker.txt'))

values ={v:k for k,v in enumerate('23456789TJQKA',2)} # v是之前的牌，k是重新定义的牌
straights = [(v,v-1,v-2,v-3,v-4) for v in (14,5,-1)]+[(14, 5, 4, 3, 2)]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

def hand_pk(hand):

    score = zip(*sorted(((v,values[k])for k,v in Counter(x[0] for x in hand).items()), reverse=True))
    score[0] = ranks.index(score[0])
    if len(set(card[1] for card in hand))==1:score[0]=5
    if score[1] in straights:score[0]=8 if score[0] ==5 else 4
    return score

print '1 win sum',sum(hand_pk(hand[:5])>hand_pk(hand[5:]) for hand in hands)
# def consecutive_method(Q):
#     T =[Q[0]]
#     for i in range(1,5):
#         T.append(Q[0]+i)
#     if T == Q:
#         return True
#     return False
#
#
# def same_method(Q,num):
#     L=set()
#     for i in Q:
#         if Q.count(i)==num:
#             L.add(i)
#     return L
#
#
# def two_pair(Q):
#     L = same_method(Q,2)
#     if len(L)==2:
#         return L
#     return 0
#
# def one_pair(Q):
#     L = same_method(Q,2)
#     if len(L)==1:
#         return L
#     return 0
#
#
# def confirm_level(L):
#     S = [10,11,12,13,14]
#     T = set()
#     Q = []
#     for j in L:
#         T.add(j[1])
#         if j[0] == 'T':
#             Q.append(10)
#         elif j[0] == 'J':
#             Q.append(11)
#         elif j[0] == 'Q':
#             Q.append(12)
#         elif j[0] == 'K':
#             Q.append(13)
#         elif j[0] == 'A':
#             Q.append(14)
#         else:
#             Q.append(int(j[0]))
#     Q.sort()
#     S.sort()
#     if len(T) == 1 and Q == S:
#         return 1
#     if len(T) == 1 and Q != S and consecutive_method(Q):
#         return 2,Q[4]
#     if same_method(Q,4):
#         return 3,same_method(Q,4)
#     if same_method(Q, 3) and same_method(Q, 2):
#         return 4,same_method(Q, 3),same_method(Q, 2)
#     if len(T) == 1:
#         return 5,Q[4]
#     if consecutive_method(Q):
#         return 6,Q[4]
#     if same_method(Q,3):
#         return 7,same_method(Q,3)
#     if two_pair(Q):
#         return 8,two_pair(Q)
#     if one_pair(Q):
#         return 9,one_pair(Q)
#     return 10,Q[4]

# print confirm_level(L)
