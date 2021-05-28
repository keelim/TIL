def palindrome(s:str, length:int) -> bool:
    for ele in range(len(s)-length+1):
        a = s[ele:ele+length]
        if a == a[::-1]:
            return True
    return False


def solution(s:str)-> int:
    n = len(s)
    if s == s[::-1]:
        return n
    else:
        for i in range(len(s), 0, -1):
            if palindrome(s, i):
                return i
        return 1