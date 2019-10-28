# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    count = 0
    for i in range (0,len(s)):
        total = 0
        for k in range(0,m):
            if i + k < len(s):
                total += s[i+k]
        if total == d:
            count += 1
    print(count)
    return count