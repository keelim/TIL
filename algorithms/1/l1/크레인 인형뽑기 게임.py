def solution(board, moves):
    answer = 0
    n = len(board)
    stack =[]
    for move in moves:
        idx = move - 1
        for i in range(n):
            if board[i][idx] != 0:
                stack.append(board[i][idx])
                board[i][idx] = 0
                break
        
        if len(stack) == 0 or len(stack) ==1:
            continue
        elif stack[-2] == stack[-1]:
            stack.pop(-1)
            stack.pop(-1)
            answer+=2
        else:
            continue

    return answer