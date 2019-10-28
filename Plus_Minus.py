# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zero += 1
        else:
            neg += 1

    print("{0:.6f}".format(pos / len(arr)))
    print("{0:.6f}".format(neg / len(arr)))
    print("{0:.6f}".format(zero / len(arr)))