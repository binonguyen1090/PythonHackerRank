# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    i = 0
    new = []
    t1 = 0
    t2 = 0
    j = len(arr) - 1
    while i < len(arr):

        t1 += arr[i][i]
        t2 += arr[i][j]

        i+=1
        j-=1
    dif = t1 - t2
    print(abs(dif))

print(diagonalDifference(([11,2,4],[4,5,6],[10,8,-12])))