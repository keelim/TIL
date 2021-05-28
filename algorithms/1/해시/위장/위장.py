
def solution(clothes):
    data = dict()

    for clothe in clothes:
        data[clothe[1]] = data.get(clothe[1], 0) + 1

    answer = 1
    for ele in data.values():
        answer *= (ele+1)
    print(answer)
    answer -= 1
    return answer
