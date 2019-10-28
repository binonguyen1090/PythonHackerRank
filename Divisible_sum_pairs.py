# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range (0,len(ar)-1):
        for j in range (i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count