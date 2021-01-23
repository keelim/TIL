def solution(numbers):
    num =[]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            num.append(numbers[i]+numbers[j])
    
    return sorted(list(set(num)))