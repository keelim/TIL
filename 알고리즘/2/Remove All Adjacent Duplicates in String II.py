class Solution:
     def removeDuplicates(self, s, k):
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return ''.join(c * k for c, k in stack)




s = Solution()
print(s.removeDuplicates(s = "abcd", k = 2))
print(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
print(s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))