class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 数値を1桁の整数のリストへ変換
        try:
            list = [int(i) for i in str(x)]
        except ValueError:
            return False

        even_flg = len(list) % 2 == 0
        for i, num in enumerate(list):
            if even_flg and i >= len(list) / 2:
                return True
            elif not even_flg and i >= len(list) / 2 - 1:
                return True
            if num != list[-(i + 1)]:
                return False
        # ここには来ない
        return False
