class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        a = b = c = 0

        for stone in stones:
            if stone % 3 == 1:
                a += 1
            elif stone % 3 == 2:
                b += 1
            else:
                c += 1

        if c % 2 == 0:
            return a > 0 and b > 0

        return abs(a - b) >= 3