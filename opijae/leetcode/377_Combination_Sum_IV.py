class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0] * (target +1)
        dp[0] = 1 # 0 + num 해서 숫자를 만들 수 있으니 dp[0]을 1로 세팅
        for i in range(target):
            for num in nums:
                if num + i <= target: # 만들 수 있는 수가 target 이하 라면 dp에 추가
                    dp[i+num] += dp[i]
        return dp[-1]