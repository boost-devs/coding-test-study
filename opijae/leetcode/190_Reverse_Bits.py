class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c =='(' or c =='[' or c =='{':
                stack.append(c)
                continue
            if len(stack)==0:
                return False
            
            temp = stack.pop()
            if temp=='(':
                if c !=')':
                    return False
            if temp=='[':
                if c !=']':
                    return False
            if temp=='{':
                if c !='}':
                    return False
        if len(stack)>0:
            return False
        return True