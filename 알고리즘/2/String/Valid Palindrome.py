class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = [ele.lower() for ele in s if ele.isalnum()]

        left = 0
        right = len(list1) - 1
        while len(list1) > 1:
            if list1.pop(0) != list1.pop(-1):
                return False

        return True

    def isPalindrome2(self, s: str) -> bool:
        import re
        s = re.sub('[^a-z0-9]', '', s)

        return s[::] ==s[::-1]
        
                