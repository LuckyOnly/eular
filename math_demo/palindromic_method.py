# coding:utf-8

# 回文
def is_pal(num):
    s = str(num)
    i = 0
    while i<int(len(s)/2):
        if s[i]!=s[len(s)-i-1]:
            return False
        i+=1
    return True
