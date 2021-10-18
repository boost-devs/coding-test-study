// 190. Reverse Bits
// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Reverse Bits.
// Memory Usage: 6 MB, less than 8.36% of C++ online submissions for Reverse Bits.

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for(int i = 0; i < 32; i++)
            if(n & ((unsigned int)1 << i)) {
                res |= ((unsigned int)1 << (32-i-1));
            }
        return res;
    }
};