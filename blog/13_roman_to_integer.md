#前書き

よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCode を始めたのであった。

一旦は Easy 問題を番号の若い順に Python で解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

3 問目

## 問題

> Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
>
> For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
>
> Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV.
>
> Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
>
> I can be placed before V (5) and X (10) to make 4 and 9.
>
> X can be placed before L (50) and C (100) to make 40 and 90.
>
> C can be placed before D (500) and M (1000) to make 400 and 900.
>
> Given a roman numeral, convert it to an integer.

面倒くさそ～～～というのが第一印象だ。

逆に、これをアルゴリズムによって簡単に表現できるのだとすればある種のワクワクのような物は感じる。

すべきことは、ローマ数字が与えられるのでそれをアラビア数字に変換する、というものだ。

それだけだとシンプルに聞こえるが、IV が 4 であるとか、考慮しないといけない事は多そうだ。

### Example

> Input: s = "MCMXCIV"
>
> Output: 1994
>
> Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## 思考プロセス

上記の MCMXCIV について考える。

アルファベット 1 文字がそれぞれ該当する数字を表すのであれば足し算なので楽だが、それぞれ対応する文字の左に I, X, C がつくとマイナスになるという感じだ。

順番に気を付ければマイナスなのか判断できそうではある。

C が 100 として登場するのは絶対に M の後なので、M より前に出てきたらマイナスにできる。

或いは、取り得る 2 つのアルファベットのペアを最初から抜き出して、それ以外を 1 文字ずつに分割すればいいだろうか。

2 つで特殊な意味をもつ組み合わせは IV, IX, XL, XC, CD, CM の 6 種類なのでそこまで多くは無い。

## 最初に提出した解

```python
from typing import Dict


class Solution:
    def romanToInt(self, s: str) -> int:
        normal: Dict[str, str] = {
            "I": "1",
            "v": "4",
            "V": "5",
            "x": "9",
            "X": "10",
            "l": "40",
            "L": "50",
            "c": "90",
            "C": "100",
            "d": "400",
            "D": "500",
            "m": "900",
            "M": "1000",
        }
        con_normal = str.maketrans(normal)
        s2 = (
            s.replace("IV", "v")
            .replace("IX", "x")
            .replace("XL", "l")
            .replace("XC", "c")
            .replace("CD", "d")
            .replace("CM", "m")
        )
        s2_list = list(s2)
        num_list = [int(n.translate(con_normal)) for n in s2_list]
        return sum(num_list)
```

## 結果

Accepted

Beats: 83.11%
Runtime: 57ms
Memory: 13.8MB

汚いというか、pythonic ではない感じがする。。
しかしどうすればいいかと言われるとこれくらいしか思いつかなかった。

解説するほどのこともしていないが、2 文字で 1 セットになる数字を 1 文字に変換し、それぞれ対応する数字に変換後に全部足しているだけだ。

Accepted にはなりそうだと思ったが、流石に的確な解法ではなさそう。

## Solutions を見る/

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        rd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        n = len(s)
        rt = 0
        for i in range(n):
            if i == n - 1 or rd[s[i]] >= rd[s[i + 1]]:
                rt += rd[s[i]]
            else:
                rt -= rd[s[i]]

        return rt
```

## 何をしているのか？

なるほどなーーーーーーーと言う気持ちになった。

要するに、次の数字より対象が大きいならそれは特殊な例なので、マイナスにしている。

最初に順番見ればできそうと思ったが、そっちのアプローチと言う感じだ。

Beats: 99.32%
Runtime: 38ms
Memory: 13.9MB

上記の結果的にもこっちの方が良さそうだ。
私の解答は変換処理があるので、それが無い分早いのは納得できる。

## どう考えるべきだったのか

これは案としては頭にあったので、どちらが早いかをもっと検討すべきだった。

考え方としてはそこまで悪くなかったのかなと言う印象ではある。
