def solution(arr):
    pointer = min(arr)
    answer = list(filter(lambda a: a!=pointer, arr))
    if(len(answer)==0):
        return [-1]
    else:
        return answer