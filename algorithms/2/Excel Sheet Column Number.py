class Solution:
    def titleToNumber(self, s: str) -> int:
        standard = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = 0

        dict1 = {ele: idx+1 for idx, ele in enumerate(standard)}
        a = 1
        while len(s) > 0:
            if(len(s) == 1):
                result += (dict1[s[-1]]*a)
                s = ''
            else:
                result += (dict1[s[-1]]*a)
                s = s[:-1]
                a *= 26
        return result
