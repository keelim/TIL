class Solution:
    def thousandSeparator(self, n: int) -> str:
        i=0 
        result =''
        if(n==0):
            return "0"
        
        while n>0:
            if i%3==0 and i!=0:
                result = '.'+result
            
            result = str(n%10) + result
            n//=10
            i+=1
            
        return result
            