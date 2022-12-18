from typing import List


class Solution:
    prefix: str = ""

    def compare(self, strs: List[str]) -> bool:
        for st in strs:
            if not st.startswith(self.prefix):
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


class SolutionHorizon:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for st in strs:
            while prefix and not st.startswith(prefix):
                prefix = prefix[:-1]
        return prefix


class SolutionVertical:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i, c in enumerate(strs[0]):
            for st in strs:
                if i == len(st) or st[i] != c:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    SolutionVertical().longestCommonPrefix(strs)
