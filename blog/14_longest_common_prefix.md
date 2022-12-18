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

与えられた文字列の配列の中身で共通している最長の接頭辞を返却するという内容。

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

共通部分を抜き出すような関数があるかと思いググっていたところ、クリティカルな答えに当たりそうだったため中止した。

ループして 1 文字ずつ調べるやり方以上にいい方法が思いつかないので、とりあえずそれで実装してみる

## 最初に提出した解

```python
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
```

## 結果

Accepted

Beats: 35.93%
Runtime: 72ms
Memory: 14MB

思っていたより遅くは無いという印象ではあるが、最適なのか？と言う疑問は残る。

もう少しやりようはあると思うが、いまいち具体的な改善案がスッと出てこない。

## Solutions を見る

ここからは私が英文の公式解説を読んで理解した内容を記述するので、内容の正しさは保証できません。悪しからず。

[元ソース](https://leetcode.com/problems/longest-common-prefix/solutions/127449/longest-common-prefix/)を見ましょう。

#### 水平走査(Horizontal scanning)

各文字列を順に比較していく方法。

私がやったのと違うのは、例えば["flower","flow","flight"]という配列の場合、"flower"を他の要素全てと比較していくのではなく、

"flower"と"flow"の共通最長接頭辞(Longest Common Prefix 解説に倣い以下 LCP)である"flow"を次の要素と比較して、、、と言うことを続けていく。

公式解説では Java の記述が載っているので、Python で記述してみる。

```python
class SolutionHorizon:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for st in strs:
            while prefix and not st.startswith(prefix):
                prefix = prefix[:-1]
        return prefix
```

おおー、簡潔だ。。。

というか私がやってたことが冗長だっただけだな。。。

私がやりたかったことの延長がこれなのだが、while 文をうまく使えてなかった。

Beats: 69.59%
Runtime: 53ms
Memory: 13.9MB

#### 垂直走査(Vertical scanning)

上の水平走査の問題は、配列の最後にごく短い LCP が存在するようなケースである。

そのネックを解決する垂直走査では、各文字の index を垂直に比較していく。

["flower","flow","flight"]という配列の場合、index=1x の f を比較していき、index=3 で"flight"が not equal になるので LCP が出る。

同様に python で実装してみる。

```python
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
```

これ全探索では？遅そうじゃない？と思った。

Beats: 13.26%
Runtime: 84ms
Memory: 13.9MB

遅かった。全探索とは違うのかな？あまりよくわからない。

## どう考えるべきだったのか

Solutions にはもう少し別の解法も載っていた。

strs を分割して、それぞれの LCP 同士の LCP を出すという方法も載っていて少し気になった。

ただ、これ以上考えてると嫌になりそうだったので終わることにする、続けることの方が大事なので。。。
