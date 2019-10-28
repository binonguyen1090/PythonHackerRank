# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, b):
    big = 0
    for i in keyboards:
        for k in drives:
            total = i + k
            if total > big and total <= b:
                big = total

    if big == 0:
        print(-1)
        return -1

    print(big)
    return big