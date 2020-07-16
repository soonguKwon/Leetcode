from typing import List
from collections import defaultdict
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_dict = defaultdict(int)
        bit_num = lambda ch: ord(ch) - ord('a')
        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << bit_num(ch)
            bit_dict[bitmask] = max(bit_dict[bitmask], len(word))

        res = 0
        for a in bit_dict:
            for b in bit_dict:
                if a & b == 0:
                    res = max(res, bit_dict[a] * bit_dict[b])
        return res
if __name__ == '__main__':
    input = ["abcw","baz","foo","bar","xtfn","abcdef"]
    s = Solution()
    print(s.maxProduct(input))