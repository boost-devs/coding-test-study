class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # 열린 괄호면 스택에 넣기
            if c =='(' or c =='[' or c =='{':
                stack.append(c)
                continue
            if len(stack)==0:
                return False
            
            temp = stack.pop()
            # 닫힌 괄호면 pop한 값이랑 비교
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
