class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        _min = min(nums)
        _max = max(nums)
        diff = _max - _min
        if diff > 10 ** 5 + 1: # nums의 길이는 10^5 만큼이다.
            diff = 10 ** 5
        arr = [0] * (diff+1)
        adnormal = [] # 최소값과 차이가 10^5 이상나는 값(이상치)들 저장
        # arr돌면서 연속된수 찾기
        for num in nums:
            idx = num - _min
            if num > _min + 10 ** 5:
                adnormal.append(num) # 이상치들 넣어두기
            elif not arr[idx]:
                arr[idx] = 1
        max_len = 0
        cnt = 0
        _max_idx = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                cnt += 1
                _max_idx = i
            elif arr[i] == 0:
                max_len = max(max_len,cnt)
                cnt = 0
        max_len = max(max_len,cnt)
        cnt = 0

        # 이상치들이 있을 경우
        if adnormal:
            adnormal.sort()
            if _max_idx == adnormal[0]+1: # 정상값(min과 차이가 10^5이하로 나는 값들)의 제일 최대값, 이상치의 최소값이 연속되었는지
                cnt += 1
            for i in range(len(adnormal)-1):
                if adnormal[i] == adnormal[i+1]+1:
                    cnt += 1
                else:
                    max_len = max(max_len,cnt)
                    cnt = 0
            max_len = max(max_len,cnt)
        return max_len

a = Solution()
nums = [100,4,200,1,3,2]
print(a.longestConsecutive(nums))