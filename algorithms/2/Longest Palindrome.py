
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1 = dict()

        for ele in s:
            dict1[ele] = dict1.get(ele, 0) + 1

        cnt = 0
        flag = False
        for key, value in dict1.items():
            cnt += (value//2*2)

            if value % 2 == 1:
                flag = True

        if flag:
            cnt += 1

        return cnt


s = Solution()
print(s.longestPalindrome('abccccdd'))
print(s.longestPalindrome('a'))
print(s.longestPalindrome('ccc'))
