# Sock Merchant
#  It must return an integer representing the number of matching pairs of socks that are available.
# Sample Input
# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output
# 3


def sockMerchant(n, ar):
    new_arr = []
    count = 0
    for i in range (0,n):
        num = ar[i]
        if new_arr.__contains__(num):
            count += 1
            new_arr.remove(num)
        else:
            new_arr.append(num)

    return count