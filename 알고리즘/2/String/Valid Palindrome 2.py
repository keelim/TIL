class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            temp = str(s[:i]) +str(s[i+1:])
            print(locals())
