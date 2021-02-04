class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict1 = {num : alpha for num, alpha in zip(range(1, 27), 'abcdefghijklmnopqrstuvwxyz')}
        # mapping 완료
        result = ''
        for i in range(len(s)):
            
            if i+2 <len(s):
                if(s[i+2]=='#'):
                    result+=dict1[int(s[i:i+2])]
                    continue

            if i+1 <len(s):
                if(s[i+1]=='#'):
                    continue
                    
            if(s[i]=='#'):
                continue
               
            result += dict1[int(s[i])]
            
        return result