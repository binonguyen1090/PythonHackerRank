# https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_a = 0
    count_o = 0
    for i in apples:
        i += a
        if s <= i <= t:
            count_a += 1
    for j in oranges:
        j += b
        if s <= j <= t:
            count_o += 1
    print(count_a)
    print(count_o)