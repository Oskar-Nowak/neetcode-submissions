class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        lp = 0
        rp = l - 1

        while lp < rp:
            if not s[lp].isalpha() and not s[lp].isnumeric():
                lp += 1
                continue
                
            if not s[rp].isalpha() and not s[rp].isnumeric():
                rp -= 1
                continue

            if s[lp].lower() != s[rp].lower():
                return False

            lp += 1
            rp -= 1

        return True