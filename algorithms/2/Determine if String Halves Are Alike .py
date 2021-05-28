class Solution:
    basic ='aeiouAEIOU'
    
    def cnt(self, s):

        return len([[ele for ele in s if ele in Solution.basic]])

    def halvesAreAlike(self, s: str) -> bool:
        
        a, b = self.cnt(str(s[:len(s)//2])), self.cnt(str(s[len(s)//2:]))
        
        return a==b
