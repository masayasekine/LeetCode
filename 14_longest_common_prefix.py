from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]

    def compare(prefix: str, strs: List[str]):
        for st in strs:
            if prefix != st:
                prefix = prefix[:-1]
                return False
        return
