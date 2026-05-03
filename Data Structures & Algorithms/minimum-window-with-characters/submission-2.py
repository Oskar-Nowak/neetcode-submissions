from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t = Counter(t)
        count_window = defaultdict(int)

        need = len(count_t)
        have = 0

        best_left = best_right = 0
        best_length = float('inf')

        l = 0
        for r in range(len(s)):
            count_window[s[r]] += 1
            if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if s[l] in count_t and count_window[s[l]] == count_t[s[l]]:
                    have -= 1

                if r - l + 1 < best_length:
                    best_length = r - l + 1
                    best_left = l
                    best_right = r

                count_window[s[l]] -= 1
                l += 1

        return s[best_left:best_right+1] if best_length != float('inf') else ""


        

