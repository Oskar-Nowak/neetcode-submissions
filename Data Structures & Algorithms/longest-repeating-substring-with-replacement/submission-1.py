class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        input_length = len(s)
        chars_counter = [0] * 26
        l = r = result = max_f =  0

        while r < input_length:
            
            chars_counter[self._calc_index(s[r])] += 1
            max_f = max(chars_counter[self._calc_index(s[r])], max_f)
            r += 1

            while (r - l) - max_f > k:
                chars_counter[self._calc_index(s[l])] -= 1
                l += 1

            result = max(r - l, result)

        return result
            
    def _calc_index(self, c: str):
        return ord(c) - ord('A')