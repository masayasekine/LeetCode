# 前書き

よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCode を始めたのであった。

一旦は Easy 問題を番号の若い順に Python で解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

4 回目。とりあえずは 3 回で終わらなくてよかった。

## 問題

『14. Longest Common Prefix』

> Write a function to find the longest common prefix string amongst an array of strings.
>
> If there is no common prefix, return an empty string "".

与えられた文字列の配列の中身で共通している最長の文字列を返却するという内容。

最初、prefix とあったので先頭の文字列限定かと思って失敗した。

## Constraints

> 1 <= strs.length <= 200
>
> 0 <= strs[i].length <= 200
>
> strs[i] consists of only lowercase English letters.

### Example

> Input: strs = ["flower","flow","flight"]
>
> Output: "fl"

それぞれ'fl'が共通しているので、それを返却する。

共通するものが無ければ空文字を返却する。

## 思考プロセス

すぐ思いつくのは、各文字列を index で比較して合うところまで返却するという方法。

でもこれは例のごとく全探索になりそうなので止めた方が良さそうだ。

条件として配列の長さは 200 以下、文字列の長さも 200 以下なので、全部一致するようなケースで計算量が増えすぎそう。

1 つの単語で他の文字列に対して re.search()して、無いやつがいたら後ろから 1 文字減らしてというのを繰り返せば全探索よりは速そう。

共通部分を抜き出すような関数があるかと思いググっていたところ、クリティカルな答えに当たりそうだったため中止した。

## 最初に提出した解

```python
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
```

## 結果

Accepted

Beats: %
Runtime: ms
Memory: MB

## もうちょい考える

## Solutions を見る/

## 何をしているのか？

## どう考えるべきだったのか
