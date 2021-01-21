class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if(len(stack)==0):
                stack.append(i)
                continue

            if(stack[-1]=='[' and i==']'):
                stack.pop()
                continue
            if(stack[-1]=='{' and i=='}'):
                stack.pop()
                continue
            if(stack[-1]=='(' and i==')'):
                stack.pop()
                continue

            stack.append(i)
        
        return len(stack)==0

class Solution:
    def isValid(self, s):
        stack = []
        dictionary = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if c in dictionary.values():
                stack.append(c)
            elif c in dictionary.keys():
                if stack == [] or dictionary[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        



        
