# coding:utf-8

db =  {};
i = 1;
while True:
    key = list(str(i**3))
    key.sort()
    key = ''.join(key)
    if db.get( key ) == None:
        db[key] = [1,i**3]
    else:
        db[key][0] += 1
        if db[key][0] == 5:
            print db[key][1]
            break
    i += 1