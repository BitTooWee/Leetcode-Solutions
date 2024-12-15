class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in magazine:
            if i not in letters:
                letters.update({i:1})
            else:
                letters.update({i:letters[i] + 1})
        for i in ransomNote:
            if i not in letters:
                return False
            else:
                letters.update({i:letters[i] - 1})
                if letters[i] == -1:
                    return False
        return True
