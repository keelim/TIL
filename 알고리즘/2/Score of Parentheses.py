class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        S = S.replace('()', '1')

        while not S.isnumeric():
            for ele in S:
                
                    
