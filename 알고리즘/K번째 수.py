def solution(array, commands):
    answer = []
    for ele in commands:
        temp = sorted(list(array[ele[0]-1:ele[1]]))
        answer.append(temp[ele[2]-1])
    return answer