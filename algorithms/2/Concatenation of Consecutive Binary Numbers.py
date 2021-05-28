def d_to_b(n):
    return bin(n).replace('0b', '')

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result=''
        for i in range(1, n+1):
            result+=d_to_b(i)
        #11011~~~~
        
        modulo = 10**9+7
        return int(result, 2) % modulo