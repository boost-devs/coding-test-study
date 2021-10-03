# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_before = [1] * len(nums)
        prod_after = [1] * len(nums)
        for i in range(1, len(nums)):
            prod_before[i] = prod_before[i - 1] * nums[i - 1]
            prod_after[-(i + 1)] = prod_after[-i] * nums[-i]
        return [a * b for a, b in zip(prod_after, prod_before)]
        