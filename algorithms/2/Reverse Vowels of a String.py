class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        basic = [ele for ele in s if ele in vowels]
        basic.reverse()        
        i=0
        result =''
        for ele in s:
            if ele not in vowels:
                result+='ele'
            else:
                result+=basic[i]
                i+=1
        return result
        
        
        
        
        
        