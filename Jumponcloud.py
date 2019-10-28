# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
def jumpingOnClouds(c):
    jump = 0
    i = 0
    while (i < len(c) -1):
        if i+2 < len(c)and c[i+2] != 1:
            jump+=1
            i+=2
        else:
            jump+=1
            i+=1
    return jump

print(jumpingOnClouds([0,0,1,0,0,1,0]))