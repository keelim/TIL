def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
      
      a1 = bin(arr1[i]).replace('ob', '')
      b1 = bin(arr2[i]).replace('ob', '')

      a1 = a1[-n:-1]
      b1 = b1[-n:-1]
      
      s = ''
      for j in range(n):
        if a1[j]=='0' and b1[j]=='0': 
          s+=' '
        else: s+='#'
      answer.append(s)

    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])