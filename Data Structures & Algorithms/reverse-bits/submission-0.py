class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bites = (n >> i) & 1
            res += bites << (31-i)

        return res