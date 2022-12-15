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
Acceptedになった。

Beats: 5.4%
Runtime: 215ms
Memory: 13.9MB

Q: LeetCode上に表示されるBeatsとは何の数値ですか？
A: 知らん。100%が上限で、高い方がいいっぽい（有識者教えてください）

# もうちょい考える
1.Two Numで詰んで密かに精神的ダメージを受けたので、とりあえず自力でAcceptedに持って行けたのは一安心ではある。（Easyは最悪Brute forceでならいけると思ってた）

とは言え、いろいろスマートでは無さそうというのは実感としてある。

しかし問題の性質上全ての数字を洗わずに正解を出すというのは難しいのではとも思い、整数変換部分以外の具体的な改善案は思いつかない。

他のアプローチがあるかもしれないので、回文の特性を考える。

1. 先頭から読んでも末尾から読んでも差異が無い(特性ではなく定義である)
2. 文字数が偶数の場合の中央の1文字を除き、登場する文字は偶数個になる

これくらいしか思いつかない。


ここまで書いて1つ思ったが、下記手順でも可能そうだ。(マジでリアルタイムで考えながら書いているのである。思考整理の目的もある。)
1. 配列化する
2. 中央で配列を2つに分割する(要素数が奇数の場合中央は消す)
3. 後者の配列を逆順に修正する
4. 2つの配列を比較する

というかこっちの方がループしなくて済むので良さそうだ。


# 第二提出案
```python
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 数値を1桁の整数のリストへ変換
        try:
            list = [int(i) for i in str(x)]
        except ValueError:
            return False

        list_a = list[: math.floor(len(list) / 2)]
        list_b = list[math.ceil(len(list) / 2) :]
        list_b.reverse()

        return list_a == list_b
```


# 結果2
Acceptedになった。

Beats: 5.4%
Runtime: 207ms
Memory: 14MB


個人的には結構いい案を思いついたと思ったのだが、結果としてはほとんど差異はなかった。

(解法に気づいたくらいのテンションだったので正直結構残念だった)

reverseの計算コストが高いのかな？原因はいまいちわからない。

ん？というか、今気づいたがreverseするならlistを分割する必要ないな。草生える。

難しく考えすぎていたな、答えを出すだけなら文字の配列にしてreverseして比較すればそれだけでよかった。


# 第三提出案

```python
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
```

# 結果3
Acceptedになった。

Beats: 87.68%
Runtime: 68ms
Memory: 13.8MB

Memoryの数値はさほど変わらないものの、3倍程度高速になった。

これが自分の中での最適解だが、とりあえずSolutionsを確認してみる。

# Solutionsを見る

以下、(Solutions)[https://leetcode.com/problems/palindrome-number/solutions/127661/palindrome-number/]より引用し翻訳


> 最初に思いつくのは、数を文字列に変換し、その文字列が回文であるかどうかを調べることである。しかし、この場合、文字列を作るために余分な非定常領域が必要となり、問題の記述では許されない。
> 
> 次に、数字そのものを反転させて、元の数字と比較し、同じであれば回文である、という考え方もあります。しかし、反転した数がint.MAXtext{int.MAX}より大きい場合、整数オーバーフロー問題にぶつかる。
> 
> 2番目の考えに基づいて、反転した数のオーバーフロー問題を避けるために、intの半分だけを反転させたらどうだろう。結局のところ、回文であれば、回文の後半部分の逆数は前半部分と同じになるはずである。
> 
> 例えば、入力が「1221」の場合、「1221」という数字の最後の部分を「21」から「12」に直して、「12」という数字の前半部分と比較すれば、12は12と同じなので、その数字が回文であることが分かります。
> 
> この考え方をアルゴリズムに置き換えるとどうなるか見てみましょう。
> 
> 
> まず、いくつかのエッジケースに注意する必要があります。例えば、-123は'-'が'3'にならないので回文にはならない。したがって、すべての負の数に対してfalseを返すことができる。
> 
> 次に、数字の後半を元に戻す方法を考えてみよう。1221という数字について、1221 % 10とすると、最後の一桁が1になってしまいます。そして、下一桁の数字を10倍して、下二桁の数字を足すと、1 * 10 + 2 = 12 となり、目的の回帰した数字が得られます。この作業を続けると、さらに桁数の多い逆数が出てくる。
> 
> さて、問題は、どうやって数字の半分に到達したことを知るかである。
> 
> 元の数字を10で割って、反転した数字に10を掛けたのだから、元の数字が反転した数字より小さければ、数字の半分の桁を処理したことになるのだ。


つまり、どういうことだってばよ・・？


# つまりどういうことか
数値をそのまま反転すればええやんけ！というのはNGらしい。

数値をそのまま反転するというのは考えてなかったが、配列化して反転したのは結果的に良かった。

負の数は全てFalseとするのもとりあえずOKだったようだ。

問題はこの辺である。

> 次に、数字の後半を元に戻す方法を考えてみよう。1221という数字について、1221 % 10とすると、最後の一桁が1になってしまいます。そして、下一桁の数字を10倍して、下二桁の数字を足すと、1 * 10 + 2 = 12 となり、目的の回帰した数字が得られます。この作業を続けると、さらに桁数の多い逆数が出てくる。

ちょっと何言ってるかわかんないですね（サンドウィッチマン）

翻訳機にかけてそのまま読んでたが、どうやら翻訳が悪そうだったので再度部分的に翻訳機にかけた（意地でも自分で読まないスタイル）

> では、数字の下半分を元に戻す方法を考えてみましょう。1221という数字について、1221 % 10とすると、下1桁が出ます。下2桁を得るには、1221から下1桁を取り除く必要がありますが、それには、1221 / 10 = 122と10で割ればよいでしょう。そして、下一桁の数字を10倍して、下二桁の数字を足すと、1 * 10 + 2 = 12 となり、目的の回帰した数字が得られます。この作業を続けると、さらに桁数の多い反数が出てくる。


あー－－－なるほど、なんとなく30%くらいわかった気がするな。

でもうまいこと言語化はできないのでコードで書こう。

公式のSolutionsではC#のコードしか載っていないので、そのまま載せる。

```C#
public class Solution {
    public bool IsPalindrome(int x) {
        // Special cases:
        // As discussed above, when x < 0, x is not a palindrome.
        // Also if the last digit of the number is 0, in order to be a palindrome,
        // the first digit of the number also needs to be 0.
        // Only 0 satisfy this property.
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber || x == revertedNumber/10;
    }
}
```


# 何をしているのか？

上のSolutionsで書いてあるとおりなのだが、自分なりに嚙み砕いてみる。

まず、エッジケースについて

これは、xが負数であるケースと、x % 10が0であり、かつxが0でないケースを弾いている。
(10の倍数が回文であることは無い)

問題はwhile以降である。

x = 1221のケースを考える

#### 1回目のループ

```revertedNumber = 0 * 10 + 1221 % 10```

revertedNumberには1が入る。

xは122
(これでクソ詰まったのだが、C#だと1221/10は122に丸められるらしい、それアリ？？？？？？？)

#### 2回目のループ

```revertedNumber = 1 * 10 + 122 % 10```

revertedNumberには12が入る

xは12

ここで```x > revertedNumber == False```になるため、ループが終了する。


#### 判定
```x == revertedNumber or x == revertedNumber / 10```
12 == 12となり、Trueになる


# これ速いの？
(Pytonで似たことをしてるSolutions)[https://leetcode.com/problems/palindrome-number/solutions/212525/python-scala-with-explanations/?q=python&orderBy=most_relevant]があったので試してみたが、そんなに早く無さそう。

結果3の方が速かった。

ただ、これは半分で処理が終わらずにreverse()を実装でやってるみたいな感じなので、公式SolutionをPythonにしたら速いのかもしれない。


# 残った疑問等
Pythonで公式Solutionを実装しようと思ったが、少数計算が面倒くさすぎて諦めてしまった。

時間がある時にやってみたい。