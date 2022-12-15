# 前書き
よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCodeを始めたのであった。

一旦はEasy問題を番号の若い順にPythonで解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

2回目の今回はタイトルの問題を解きます

# 問題
Given an integer x, return true if x is a palindrome, and false otherwise.

palindromeは回文のことであり、つまり与えられたのが前後を入れ替えても同様に読める数値である場合はtrue,そうでなければfalseというはなし。


## Example
> Input: x = 121

> Output: true

> Explanation: 121 reads as 121 from left to right and from right to left.


特に条件に付いてわかりにくい事はない(主観)


# 思考プロセス
シンプルに考えると、数値を1桁ずつ分割して配列化し、先頭と末尾から見ていって偶数個ならn/2, 奇数個ならn/2 - 1回見た時点で全てequalであればtrueとなる。

それで絶望的に計算量が多くなる気もあまりしないので、とりあえずその方向で実装してみる。


# 詰まった点

### 整数への変換
まず、数値を1桁の整数のリストへ変換する処理で少し悩んだ。

リスト内包表記でやればできるが、不要な型変換をするのはスマートではないと思ったからだ。

少し調べた結果、理解できる形で実現できるのは内包表記だと思ったためそのままいくことにした。


### ValueError
```list = [int(i) for i in str(x)]```としテストを実行したところ、下記のようなエラーになった。

> ValueError: invalid literal for int() with base 10: '-'

最初はよくわからなかったが、テストケースを見て気づいた。

```-121```というケースがあり、マイナス符号が数値変換できないためエラーになっているのだった。

これは、変換できない記号が含まれている時点でNGでも問題無い気はする(-121-という数値は存在しない為)ので、ハンドリングを追加する。


# 最初に提出した解
```python
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
            # 末尾から取る場合は-1スタートになる為+1する。
            if num != list[-(i + 1)]:
                return False
        # ここには来ない
        return False
```

 
# 結果




# もうちょい考える



# Solutionsを見る



# 何をしているのか？



# どう考えるべきだったのか

