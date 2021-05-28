class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        for ele in range(len(s)-1):
            a, b = dict1[s[ele]], dict1[s[ele+1]]
            if a < b:
                result -= a
            else:
                result += a

        result += dict1[s[len(s)-1]]
        return result


s= Solution()
a= s.romanToInt("III")
print(a)
