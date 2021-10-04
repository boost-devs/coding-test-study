# 문제: 128. Longest Consecutive Sequence
# 링크: https://leetcode.com/problems/longest-consecutive-sequence/


# 시간/공간: 237ms / 25.9MB
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 길이가 1이하라면
        if len(nums) <= 1:
            return len(nums)

        count = 1  # 연속 시퀀스 길이
        max_length = 1  # 최대 연속 시퀀스 길이
        sorted_nums = sorted(set(nums))  # 고유한 요소에 대해 정렬

        for i in range(1, len(sorted_nums)):
            # 연속 시퀀스를 이룬다면
            if sorted_nums[i - 1] == sorted_nums[i] - 1:
                count += 1  # 길이 갱신
            # 아니라면
            else:
                max_length = max(max_length, count)  # 최대 길이 갱신
                count = 1  # 길이 초기화
        max_length = max(max_length, count)  # 마지막 요소에 대한 갱신
        return max_length
