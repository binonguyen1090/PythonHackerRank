# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def beautifulDays(i, j, k):
    count = 0
    for n in range (i,j+1):
        new = res(n)
        if (abs(n-new) % k) == 0:
            count += 1
    print(count)
    return(count)


def res(n):
  cop = n
  rev = 0
  while cop > 0:
    rev = rev*10 + cop%10
    cop = int(cop/10)
  return(rev)