answer = 0


def go(index, cnt, numbers, target):
    global answer
    if index == len(numbers):
        if cnt == target:
            answer += 1
    if index >= len(numbers):
        return

    go(index+1, cnt+numbers[index], numbers, target)
    go(index+1, cnt-numbers[index], numbers, target)


def solution(numbers, target):
    go(0, 0, numbers, target)
    return answer
