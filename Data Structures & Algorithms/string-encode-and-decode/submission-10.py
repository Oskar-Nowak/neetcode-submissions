class Solution:
    def __init__(self):
        self.lengths = []

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            self.lengths.append(len(s))
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:   
        decoded_list = []
        total_len = current_index = 0
        for l in self.lengths:
            decoded_list.append("")
            for i in range(total_len, l + total_len):
                decoded_list[current_index] += s[i]
            current_index += 1
            total_len += l
        return decoded_list