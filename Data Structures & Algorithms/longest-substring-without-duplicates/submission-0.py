class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        l = r = 0
        longest_substring = 0
        unique_chars = set()
        while r < length:
            if s[r] not in unique_chars:
                unique_chars.add(s[r])
                r += 1
            else:  # Element is present in our set
                while s[r] in unique_chars:
                    unique_chars.remove(s[l])
                    l += 1
            longest_substring = max(longest_substring, (r - l))
        return longest_substring