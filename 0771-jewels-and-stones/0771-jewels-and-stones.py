class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d ={}
        for i in stones:
            if i in d.keys():
                d[i]+=1
            else:
                d[i] = 1
        count = 0
        for i in d.keys():
            if i in jewels:
                count+=d[i]

        return count
    

        