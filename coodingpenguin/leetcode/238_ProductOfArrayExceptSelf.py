# 문제: 238. Product of Array Except Self
# 링크: https://leetcode.com/problems/product-of-array-except-self/


# 시간/공간: 248ms / 22.4MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 앞에서 부터 시작해 누적곱 계산
        left = [nums[0]]
        for i in range(1, n):
            left.append(left[-1] * nums[i])

        # 뒤에서 부터 시작해 누적곱 계산
        right = [nums[-1]]
        for i in range(n - 2, -1, -1):
            right.append(right[-1] * nums[i])
        right.reverse()

        answer = [right[1]]
        for i in range(1, n - 1):
            # i를 제외한 곱 계산
            answer.append(left[i - 1] * right[i + 1])
        answer.append(left[n - 2])
        return answer


# 시간/공간: 240ms / 21.2MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # 정답 배열
        left = right = 1  # 앞, 뒤 누적곱

        for i in range(n):
            j = n - left - 1  # 포인터
            answer[i] *= left
            answer[j] *= right
            left *= nums[i]
            right *= nums[j]
        return answer
