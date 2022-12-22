from collections import deque


class Solution:
    def isValidSolutions(self, s: str) -> bool:
        dic = {"(": 1, ")": 2, "[": 3, "]": 6, "{": 5, "}": 10}
        res = deque()
        for one in s:
            temp = dic[one]
            if temp % 2:
                res.append(temp)
            else:
                if not res or res.pop() != temp // 2:
                    return False
        return not res

    def isValidMyAns(self, s: str) -> bool:
        brackets = {"(": ")", "[": "]", "{": "}"}

        q = deque()
        for c in s:
            if c in brackets.keys():
                q.append(c)
            else:
                if not q or c != brackets[q.pop()]:
                    return False
        return not q and True
