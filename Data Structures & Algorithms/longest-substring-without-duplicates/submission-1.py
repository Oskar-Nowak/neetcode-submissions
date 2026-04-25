class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        l = r = 0
        longest_substring = 0
        unique_chars = set()
        while r < length:
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            
            unique_chars.add(s[r])
            r += 1
            longest_substring = max(longest_substring, (r - l))
        return longest_substring