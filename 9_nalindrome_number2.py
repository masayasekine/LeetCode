import copy


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 数値を1桁の整数のリストへ変換
        try:
            list = [int(i) for i in str(x)]
        except ValueError:
            return False
        list_b = copy.copy(list)
        list_b.reverse()

        return list == list_b
