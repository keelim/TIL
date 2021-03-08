def solution(s):
    stack = []

    for ele in s:
        if len(stack)==0:
            stack.append(ele)
            continue

        if (stack[-1] == '(' and ele == ')') or (stack[-1] == '{' and ele == '}'):
            stack.pop(-1)
            continue
        else:
            stack.append(ele)
            continue

    return True if len(stack) == 0 else False