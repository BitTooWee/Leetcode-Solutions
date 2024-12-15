class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in letters:
                letters.update({i:letters[i]+1})
            else:
                letters.update({i:1})
        for i in t:
            if i in letters:
                letters.update({i:letters[i]-1})
                if letters[i] < 0:
                    return False
            else:
                return False
        return True
