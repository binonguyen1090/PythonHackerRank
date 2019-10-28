# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    new = sorted(arr)
    min = 0
    big = 0
    for i in range(0,4):
        min += new[i]
    for k in range(1,5):
        big += new[k]
    print(min,big)