def solution(n, arr1, arr2):
    answer = []
    
    for ele in range(n):
      a = bin(arr1[ele]|arr2[ele]).replace('0b', '').rjust(n, '0').replace('1', '#').replace('0', ' ')
      answer.append(a)
    return answer



solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
