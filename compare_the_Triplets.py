
# https://www.hackerrank.com/challenges/compare-the-triplets/problem
def compareTriplets(a, b):
    ali = 0
    bob = 0
    for i in range (0,len(a)):
        if a[i] > b[i]:
            ali += 1
        elif a[i] < b[i]:
            bob += 1
    return (ali, bob)