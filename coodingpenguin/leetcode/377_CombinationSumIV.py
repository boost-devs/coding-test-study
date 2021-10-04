# 문제: 377. Combination Sum IV
# 링크: https://leetcode.com/problems/combinations-sum-iv/


# 시간/공간: 48ms / 14.2MB
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        table = [0] * (target + 1)
        for i in range(target + 1):
            # nums 자기 자신으로 만들 수 있으므로
            if i in nums:
                table[i] += 1  # +1 증가
            # nums를 사용하여
            for j in nums:
                # 범위 내라면
                if i - j > 0:
                    # 그 전 테이블 정보를 가져와 더함
                    table[i] += table[i - j]
        return table[target]
