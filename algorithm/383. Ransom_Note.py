class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = {}

        for ch in magazine:
            if ch not in magazine_map:
                magazine_map[ch] = 1
            else:
                magazine_map[ch] += 1

        for ch in ransomNote:
            if ch not in magazine_map or magazine_map[ch] == 0:
                return False
            else:
                magazine_map[ch] -= 1

        return True
