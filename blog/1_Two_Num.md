# 前書き
よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCodeを始めたのであった。

一旦はEasy問題を番号の若い順にPythonで解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

# 問題
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
> 整数numsの配列と整数targetが与えられたとき、2つの数値の足し算がtargetになるようなインデックスを返せ。

> 各入力は正確に1つの解を持つと仮定してよく、同じ要素を2度使ってはならない。

> また、同じ要素を2度使ってはならない。解答はどのような順序でも返すことができる。


## Example
> Input: nums = [2,7,11,15], target = 9

> Output: [0,1]

> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

つまり、渡された配列numsの中から、足してtargetの数値になるペアを見つけ、それぞれのindexを返すという問題らしい。

# 最初に考えた解

``` twoSum.py
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_a in enumerate(nums):
            for j, num_b in enumerate(nums):
                if i == j:
                    continue
                if num_a + num_b == target:
                    return [i, j]
        return []
```
 
# 結果

**Time Limit Exceeded**

そらそうよなという感じである。

やったことと言えば全部回して足していって該当のペアが見つかったら返すという典型的なBrute forceであり、いくら計算量に疎い私でも適切な解だと思ったわけではない。


# もうちょい考える

どう考えても2重のループはやりすぎなので、1つにできれば良さそう。

targetとnumの比較をしてnumが大きければスキップというような小手先の高速化は思いついても、そういうことではないのはわかる。

エラーになったケースは1~10000までの数値が配列で渡され、targetは19999。

つまり、最後の2つの数値を足すのが解なので、頭から回すのではどう足掻いても間に合わなさそう。

なんかいい感じに並列処理とかするのか？と考えたが、おそらくこれは知らない類のやつで考えてもどうにもならなそうなので他人の解答を見ることに。

# Solutionsを見る
[Solutions](https://leetcode.com/problems/two-sum/solutions/127810/two-sum/)を見たところ、hashmap(dict)を使用するパターンが王道のようだった。

とりあえずほぼコピペしてみる。

```
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []
```

# 何をしているのか？

hashmapという名称で初期化したdictに、
```hashmap[num] = i```を設定する

これは、Exampleの例だと

```
{
  2: 1,
  7: 2,
  11: 3,
  15: 4
}
```
という与えられた数値とindexの組み合わせを持つdictになる。

その後、再びlistをループしながら``` complement = target - num ```を出す。

その次の

``` if complement in hashmap and hashmap[complement] != i:```

で、``` target - num ```された値(つまり、ペアの相方)がいるか判定し、加えてそれが自身でないことも判定する。

結果的に、計算量は全探索していた時と比べると激減し、Acceptedとなった。

# どう考えるべきだったのか

「計算して確かめる」というアプローチしか思いつかず、それが間違っていた。

アルゴリズムというか、普通に論理的な思考力が足りていないなと痛感。。

値とindexのペアのdictを作ってそこから探すというのは色んな所で使えそう。

次回これに気づければOKです(ポジティブ)