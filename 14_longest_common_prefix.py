from typing import List


class Solution:
    prefix: str = ""

    def compare(self, strs: List[str]) -> bool:
        for st in strs:
            if self.prefix not in st:
                self.prefix = self.prefix[:-1]
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.prefix = strs[0]
        if len(strs) == 1:
            return self.prefix
        while True:
            if not self.prefix:
                break
            if self.compare(strs):
                break
        print(self.prefix)
        return self.prefix


if __name__ == "__main__":
    strs = ["c","acc","ccc"]
    Solution().longestCommonPrefix(strs)
