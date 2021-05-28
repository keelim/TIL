class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        
        if(len(a)!=len(b)):
            return False
        
        for i in range(len(a)):
            if(a[i]!=b[i]):
                return False
            
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        counter =[0 for _ in range(26)]

        for i in range(len(s)):
            counter[s[i]-'a']+=1
            counter[t[i]-'a']-=1

        for ele in counter:
            if(ele!=0):
                return False
        return True  
    