
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(ar):
    tall = tallest(ar)
    count = 0
    for i in ar:
        if i == tall:
            count += 1
    print(count)
    return count


def tallest(ar):
    i = 0
    tallest = ar[0]
    while i < len(ar):
        if ar[i] > tallest:
            tallest = ar[i]
        i += 1
    return tallest