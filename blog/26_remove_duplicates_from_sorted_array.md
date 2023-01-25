# 前書き

よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCode を始めたのであった。

一旦は Easy 問題を番号の若い順に Python で解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

7回目、まだあまり進歩は感じない。

## 問題

> Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
> Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
> More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
> Return k after placing the final result in the first k slots of nums.
>Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

ソート済みの数値配列が与えられるので、重複する値を削除した後、ユニークな値の個数を返却するという内容

別の配列を用意するのはNGで、与えられた物を加工する必要があるらしい

## 思考プロセス

とりあえずループしていく方法を検討したが、ループの中で要素を削除するという事をしたことが無かったので少し手間取った。

ズレが出ないように要素を削除しつつ全探索するようにしたところ、下記のような実装になった。

## 最初に提出した解

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        i = 0
        while i < len(nums):
            if i != 0 and nums[i] == nums[i-1]:
                del nums[i-1]
                i -= 1
            else:
                cnt += 1
            i += 1
        return cnt
```

## 結果

Accepted

Beats: 48.52%
Runtime: 156ms
Memory: 15.5MB

## もうちょい考える

うーん、そろそろ遅いのわかりつつとりあえず全探索を提出するのやめたいな。

pythonならnumpy辺りに重複を削除する関数があるような気もしたが、クリティカルな解答が出てきそうだったので調べなかった。

調べたらnumpy.uniqueというドンピシャの関数があったが、これは使用できなかった。

詳しくはわからないが計算量敵にNGなのかな。

## Solutions を見る

## 何をしているのか？

## どう考えるべきだったのか
