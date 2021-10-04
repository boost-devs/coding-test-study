class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = 0 # 현 지점에서 갈수 있는 거리
        for i in range(len(nums)-1):
            fuel = max(fuel, nums[i]) # 갈 수 있는 거리 비교
            if fuel == 0: # 다음지점으로 갈 수 없으면
                return False
        fuel -= 1 # 다음지점으로 가니 --
        return True