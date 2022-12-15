# 前書き

よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCodeを始めたのであった。

一旦はEasy問題を番号の若い順にPythonで解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

3問目

## 問題

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. 

Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.

X can be placed before L (50) and C (100) to make 40 and 90.

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

面倒くさそ～～～というのが第一印象だ。

逆に、これをアルゴリズムによって簡単に表現できるのだとすればある種のワクワクのような物を感じる。

すべきことは、ローマ数字が与えられるのでそれをアラビア数字に変換する、というものだ。

それだけだとシンプルに聞こえるが、IVが4であるとか、考慮しないといけない事は多そうだ。

### Example

> Input: s = "MCMXCIV"
>
> Output: 1994
>
> Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## 思考プロセス

上記のMCMXCIVについて考える。

アルファベット1文字がそれぞれ該当する数字を表すのであれば足し算なので楽だが、それぞれ対応する文字の左にI, X, Cがつくとマイナスになるという感じだ。

順番に気を付ければマイナスなのか判断できそうではある。

Cが100として登場するのは絶対にMの後なので、Mより前に出てきたらマイナスにできる。

或いは、取り得る2つのアルファベットのペアを最初から抜き出して、それ以外を1文字ずつに分割すればいいだろうか。

2つで特殊な意味をもつ組み合わせはIV, IX, XL, XC, CD, CMの6種類なのでそこまで多くは無い。

## 最初に提出した解

## 結果

## もうちょい考える

## Solutionsを見る/

## 何をしているのか？

## どう考えるべきだったのか
