# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    count = 0
    limit = max(b)

    for i in range (1, limit + 1):
        if a_condition(a,i) and b_condition(b,i):
            count += 1
    print(count)


def a_condition(a,i):
    for v in a:
        if i % v != 0:
            return False
    return True

def b_condition(b, i):
    for v in b:
        if v % i != 0:
            return False
    return True

getTotalX([2,4],[16,32,96])
