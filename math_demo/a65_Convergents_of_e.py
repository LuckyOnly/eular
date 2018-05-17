#Project Euler Problem 65

n0, n1, L = 1, 2, 100

for i in xrange(2, L+1):
    n0, n1 = n1, n0 + n1 * (1 if i%3 else 2 * i//3)

print "Project Euler 65 Solution =", sum(map(int, str(n1)))