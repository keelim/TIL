def solution(n):
    s=''
    while n>0:
        s = str(n%3)+s
        n = n//3
    tmp = s[::-1]

    a = 0
    b = 1
    for i in range(len(tmp)-1, -1, -1):   
        a+= (int(tmp[i]))*b
        b*=3

    return a