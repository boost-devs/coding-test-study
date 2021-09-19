# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ordered_nums = sorted((k, i) for i, k in enumerate(nums))
        start, end = 0, len(nums) - 1
        while start < end:
            two_sum = ordered_nums[start][0] + ordered_nums[end][0]
            if two_sum < target:
                start += 1
            elif two_sum > target:
                end -= 1
            else:
                return [ordered_nums[start][1], ordered_nums[end][1]]
                