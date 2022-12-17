# 前書き

よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCode を始めたのであった。

一旦は Easy 問題を番号の若い順に Python で解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

4回目。とりあえずは3回で終わらなくてよかった。

## 問題

『14. Longest Common Prefix』

> Write a function to find the longest common prefix string amongst an array of strings.
>
> If there is no common prefix, return an empty string "".

与えられた文字列の配列の中身で共通しているprefixを返却するという内容。

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

すぐ思いつくのは、各文字列をindexで比較して合うところまで返却するという方法。

でもこれは例のごとく全探索になりそうなので止めた方が良さそうだ。

条件として配列の長さは200以下、文字列の長さも200以下なので、全部一致するようなケースで計算量が増えすぎそう。

1つの単語で他の文字列に対してre.search()して、無いやつがいたら後ろから1文字減らしてというのを繰り返せば全探索よりは速そう。

ただ、その場合全部完全に異なる文字列だった場合に遅そうだ。

共通部分を抜き出すような関数があるかと思いググっていたところ、クリティカルな答えに当たりそうだったため中止した。

一旦は自力で思いつける範囲の、ループして比較する方法を検討する。

## 最初に提出した解

## 結果

Accepted

Beats: %
Runtime: ms
Memory: MB

## もうちょい考える

## Solutions を見る/

## 何をしているのか？

## どう考えるべきだったのか
