# 문제: 20. Valid Parentheses
# 링크: https://leetcode.com/problems/valid-parentheses/


# 시간/공간: 49ms / 14.4MB
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        idx = dict(zip("(){}[]", range(6)))  # 괄호 별 번호 부여
        for letter in s:
            # 스택에 요소가 있고 닫는 괄호이고 같은 종료인 경우
            if stack and idx[letter] % 2 and idx[stack[-1]] == idx[letter] - 1:
                stack.pop()  # 가장 위에 있는 요소 제거
            # 그 외의 경우
            else:
                stack.append(letter)  # 문자 추가
        # 모든 문자를 다 돌고 요소가 남아 있다면
        if stack:
            return False  # 유효하지 않은 괄호
        return True  # 유효한 괄호
