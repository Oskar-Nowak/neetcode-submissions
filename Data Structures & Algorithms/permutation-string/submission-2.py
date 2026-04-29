class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False

        l = 0
        r = s1_length

        s1_count = [0] * 26
        for c in s1:
            s1_count[self._idx(c)] += 1
        while r < s2_length + 1:
            s2_count = [0] * 26
            for c in s2[l:r]:
                s2_count[self._idx(c)] += 1
            if s1_count == s2_count:
                return True
        
            l += 1
            r += 1

        return False
            
    def _idx(self, c: str) -> int:
        return ord(c) - ord('a')