# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    anna_no = bill[k]
    total = 0
    for i in bill:
        total += i
    anna_pay = (total - anna_no)/2
    if (b == anna_pay):
        print("Bon Appetit")
        return "Bon Appetit"
    diff = int(b - anna_pay)
    print (diff)
    return diff