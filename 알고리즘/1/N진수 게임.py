number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C'
    ,'D', 'E', 'F'
]
def number_to_n(num, n):
    result=''
    if(num==0):
        return '0'

    while num>0:
        result = number[num%n]+result
        num/=n
        
    return result

def solution(n, t, m, p):
    answer = ''
    temp =''

    mt = m*t

    i = 0
    while len(temp)<=mt:
        ngame = number_to_n(i, n)
        temp+=ngame
        i+=1
    
    for i in range(t):
        answer+=temp[(m*i)+(p-1)]

    return answer