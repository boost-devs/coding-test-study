# 문제: 217. Contains Duplicate
# 링크: https://leetcode.com/problems/contains-duplicate/


# 시간/공간: 120ms / 19.9MB
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
