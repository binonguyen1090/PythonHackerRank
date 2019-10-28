# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    big = scores[0]
    small = scores[0]
    count_big = 0
    count_small = 0
    i = 1
    k = 1
    while i < len(scores):
        if scores[i] > big:
            big = scores[i]
            count_big += 1
        i+= 1
    while k < len(scores):
        if scores[k] < small:
            small = scores[k]
            count_small += 1
        k+= 1
    print(count_big, count_small)
    return (count_big, count_small)