class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.isspace():
            return 0
        data = s.split(" ")
        return len(data[-1])