
# https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    t1 = x1
    t2 = x2
    if x1 > x2 & v1 > x2:
        print("NO")
        return "NO"
    elif x2 > x1 & v2 > v1:
        print("NO")
        return "NO"
    else:
        jump = 0
        while jump <= 10000:
            t1 += v1
            t2 += v2
            if t1 == t2:
                print("YES")
                return "YES"
            jump += 1
    print("NO")
    return "NO"