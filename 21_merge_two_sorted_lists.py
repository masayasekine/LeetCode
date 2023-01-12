# Definition for singly-linked list.
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
