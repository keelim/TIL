def palindrome(string, length):
    for i in range(len(string)-length+1):
        a = string[i:i+length]
        if a[::] ==a[::-1]:
            return True
    return False

def solution(s):
    n = len(s)
    for i in range(len(s), 0, -1):
        if palindrome(s, i) == True:
            return i
    else:
        return 1