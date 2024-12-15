class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jeweldict = {}
        for i in jewels:
            jeweldict.update({i:0})
        for i in stones:
            if i in jeweldict:
                jeweldict.update({i:jeweldict[i] + 1})
        sum = 0
        for i in jeweldict:
            sum += jeweldict[i]
        return sum
