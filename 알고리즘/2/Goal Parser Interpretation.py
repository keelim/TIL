class Solution:
    def interpret(self, command: str) -> str:
        stack =[]
        result =''
        for ele in command:
            if ele=='G':
                result+='G'
                continue
            
            if ele=='(':
                stack.append('(')
                continue
            
            if stack[-1] == '(' and ele==')':
                result+='o'
                continue

            if stack[-1]=='l' and ele ==')':
                result+='al'
                stack.pop()
                stack.pop()
                stack.pop()
                continue

            stack.append(ele)
        
        return result
                