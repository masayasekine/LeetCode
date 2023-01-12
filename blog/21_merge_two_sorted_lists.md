# 前書き

よわよわばっくえんどえんじにゃーである筆者が、そろそろちゃんとアルゴリズムやんないとやべーじゃんとなり、LeetCode を始めたのであった。

一旦は Easy 問題を番号の若い順に Python で解いていく予定。

いつまで続くかもわからないが、せっかくなら記事に残そうということで連載を開始。

新年一発目、だがかなりサボったな。。

DaD の α テストや tarkov が存外面白かったり、年末年始のゴタゴタがあったりで仕方ない、むしろ失踪しなかったのは偉い（ポジティブ）

## 問題

21. Merge Two Sorted Lists

> You are given the heads of two sorted linked lists list1 and list2.
>
> Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
>
> Return the head of the merged linked list.

### Example

> Input: list1 = [1,2,4], list2 = [1,3,4]
>
> Output: [1,1,2,3,4,4]

シンプルに 2 つのリストをマージ・ソートするという内容

## 思考プロセス

これ簡単じゃないか？と思った。

Python なら sorte 関数があるので、単純にそれでいいのではないか。

と思ったが、list1,2 はシンプルな数字のリストではなく ListNode クラスのリストになっていた。

ListNode クラスは val と Next を持ち、返却する型も`Optional[ListNode]`である必要がある。

ソートアルゴリズム、知らね〜〜〜(Final Fantasy)という感情である。

とりあえず思いつくのはこれを普通の list になんとか変換する方法かな。

## 最初に提出した解

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            if not list2:
                return []
            else:
                return list2
        simpleList1 = [node.val for node in list1]
        simpleList2 = [node.val for node in list2]
        simpleMergedList = sorted(simpleList1.extend(simpleList2))
        mergedNodeList = []
        for i in range(len(simpleMergedList)):
            if i == 0:
                continue
            node = ListNode(
                val = simpleMergedList[i-1],
                next = simpleMergedList[i]
            )
            mergedNodeList[i] = node
        return mergedNodeList
```

## 結果

> TypeError: 'ListNode' object is not iterable

なんか勘違いしていた

てっきり「node,value を持つクラスのリスト」かと思っていたが、`Optional[NodeList]`なので引数は NodeList そのものだった

じゃあ Example のはどういう事・・・？

問題文の日本語が理解できない、国語 5 なのに・・・英語だけど・・・

## Solutions を見る

マジで混乱したので Solutions を見た

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        elif list1 == None and list2 == None:
            return None
        elif list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
```

## 何をしているのか？

あ、そういうことか。

ListNode の Next には次の ListNode が入っているんだな。

普通に理解力が欠如していた。

2 つの value を比較する関数内で再起的に自信を呼び出していき、どちらかが None になったら終わるという感じ。

## どう考えるべきだったのか

問題の意図を読み取れないのは不慣れなのが問題だとは思う。

それはさておくにしても、このやり方は思いつかなかったと思う。

再帰関数作るの苦手なんだよな、多分ちゃんと理解できてないから応用できないんだと思う。

一度ちゃんと学ぶ必要があるな。
