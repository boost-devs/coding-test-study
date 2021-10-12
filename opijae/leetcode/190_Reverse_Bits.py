class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        mul = 1
        for num in str(bin(n))[2:].zfill(32):
            ans += (int(num) * mul)
            mul *= 2
        return ans
    def reverseBits_bin(self, n: int) -> int:
        return int(f"{n:032b}"[::-1],2) # f"{n:032b}" -> n을 2진수로 바꾸고 32자리수 만큼 0으로 패딩

    def reverseBits_shift(self, n: int) -> int:
        shift = 31
        result = 0
        while n != 0:
            result += (n & 1) << shift # 현재 비트에 2**shift 만큼 곱함
            n >>= 1 # 비트 이동
            shift -= 1 # 자리수 --
        return result
a = Solution()
n = 43261596
print(a.reverseBits_shift(n))