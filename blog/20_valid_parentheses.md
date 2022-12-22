# 前書き

よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCode を始めたのであった。

一旦は Easy 問題を番号の若い順に Python で解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

5 回目

最近アルゴリズムの本を読み始めてみた。

問題を解き進める日と技術書を読み進める日に別れそう、毎日１問以上解く人すげーーーという感情。

## 問題

> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
>
> An input string is valid if:
>
> Open brackets must be closed by the same type of brackets.
>
> Open brackets must be closed in the correct order.
>
> Every close bracket has a corresponding open bracket of the same type.

Example を見ただけだと'({})'のようなケースが OK なのかわからないが、文章的にも問題的にも恐らく OK だと思った。

## 思考プロセス

しばらく考えて、stack が使える気がした。

出てきた open bracket を stack に入れて、close が出てきた時に stack から 1 つ取り出して比較する。

括弧は順番通りに閉じられるので、対応する括弧でなければ NG という形。

最後は stack が空になっていることを確認すれば、全ての brackets が正常に閉じられていることがわかる。

## 最初に提出した解

```python
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        q = deque()
        for c in s:
            if c in brackets.keys():
                q.append(c)
            else:
                if not q or c != brackets[q.pop()]:
                    return False
        return not q
```

今までで一番自信があるかも。

これ以上なんとかしようがあるのか？という気持ち。

## 結果

Accepted

Beats: 79.83%
Runtime: 38ms
Memory: 13.8MB

自力で 50ms を切れたのは初めてな気がするので、素直に嬉しい。

能力の向上の結果というよりはたまたま思いついたという感じではあるが、まあいいでしょう。

## もうちょい考える

正常系の時に全文字を処理しないといけないのは、あまり良くないのかなという気はする。

しかしこの問題は最大 10000 文字なので、全文字処理してもこのくらいで済むのかという感想。

（10000 文字の正常系がケースとしてあったのかはわからないが）

とはいえ自力でこれ以上高速化できる気はしないので、大人しく先人の叡智に頼ることにする。

## Solutions を見る

公式の Solutions は有料プラン専用だったので、python で search して上に出たものを見てみる。

```python
    def isValid(self, s: str) -> bool:
        dic = {'(':1 , ')':2 , '[':3 , ']':6 , '{':5 , '}':10}
        res = []
        for one in s:
            temp = dic[one]
            if(temp %2 ):
                res.append(temp)
            else:
                if(len(res) and res[-1]==temp//2):
                    del res[-1]
                else:
                    return False
        return res==[]
```

Beats: 82.31%
Runtime: 37ms
Memory: 13.8MB

## 何をしているのか？

open と close の判定方法が面白いなと思った。

ただ、list でやるより deque の方が早いという認識だったので、微妙に腑に落ちない。

私が`brackets.keys()`で open の判定をしているのがちょっと遅いのかもな。。。

少し気になったので、この考えを流用してより高速にできるのか検討してみる。

## 融合

```python
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
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
```

Beats: 99.60%
Runtime: 22ms
Memory: 13.8MB

おおーーーー、めっちゃ早くなった。

これは面白いな、やはり deque の方が早いという私の認識は合っていて、私の実装のボトルネックは先述の判定部分だったのだと思う。

ちなみに list が deque より遅いのは、list で pop と同じことをすると、残りの要素全ての位置を変更するような処理になるためらしい。

## どう考えるべきだったのか

これは考え付かなかったなーと思う。

2 個のペアを考える時はこのやり方を思い出してみよう。

とはいえ、最後に書いたものを 100 点とするなら 90 点くらいの状態には自力で持って行けたのではないか。

満足度は高めだった。
