#https://www.hackerrank.com/challenges/strange-advertising/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import math
def viralAdvertising(n):
    new = [2]
    if n == 1:
        print(2)
        return(2)

    i = 0
    total = 2 
    while i < n-1:
        new.append(math.floor(new[-1]*3/2))
        total += new[-1]
        i+=1
    
    print(total)
    return(total)
