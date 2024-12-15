class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        for i in text:
            if i not in letters:
                letters.update({i:1})
            else:
                letters.update({i:letters[i] + 1})
        #1b1a2l2o1n
        Count = [0,0,0,0,0]
        if 'b' in letters:
            Count[0] = letters['b']
        if 'a' in letters:
            Count[1] = letters['a']
        if 'l' in letters:
            Count[2] = int(math.floor(letters['l']/2))
        if 'o' in letters:
            Count[3] = int(math.floor(letters['o']/2))
        if 'n' in letters:
            Count[4] = letters['n']
        return min(Count)
