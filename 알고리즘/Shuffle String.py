
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        di = dict()
        for i in range(len(s)):
            di[indices[i]] = s[i];
        
        a=''
        for i in range(len(s)):
           a+=di[i] 
        return a
    
    def restoreString2(self, s: str, indices: List[int]) -> str:
        A = [''] * len(s)
        for i, c in zip(indices, s):
            A[i] = c
        return "".join(A)
        