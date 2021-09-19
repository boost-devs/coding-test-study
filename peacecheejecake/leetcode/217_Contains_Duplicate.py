# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for num in nums:
            if num in memo:
                return True
            memo.add(num)
        return False
        