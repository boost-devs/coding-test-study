# 문제: 55. Jump Game
# 링크: https://leetcode.com/problems/jump-game/


# 시간/공간: 480ms / 15.4MB
# 참고: https://leetcode.com/problems/jump-game/discuss/596454/Python-Simple-solution-with-thinking-process-Runtime-O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1  # 고려할 마지막 위치
        for i in range(len(nums) - 2, -1, -1):
            # 현재 위치에서 마지막 위치까지 커버 가능하다면
            if i + nums[i] >= last_pos:
                last_pos = i  # 마지막 위치 갱신
        return last_pos == 0
