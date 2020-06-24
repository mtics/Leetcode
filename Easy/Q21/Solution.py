# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        merged_list = list()

        while True:

            if l1 is None or l2 is None:
                merged_list.append(l1 if (l2 is None) else l2)

                for i in range(len(merged_list)-1):
                    merged_list[i].next = merged_list[i+1]

                return merged_list[0]

            if l1.val < l2.val:
                merged_list.append(l1)
                l1 = l1.next
            else:
                merged_list.append(l2)
                l2 = l2.next


if __name__ == "__main__":
    solution = Solution()

    l1 = ListNode()
    l2 = ListNode()

    n1 = [1, 2, 4]
    n2 = [1, 3, 4]

    li1 = list()
    li2 = list()

    for num in n1:
        temp = ListNode(next=ListNode())
        temp.val = num
        li1.append(temp)

    for num in n2:
        temp = ListNode(next=ListNode())
        temp.val = num
        li2.append(temp)

    for i in range(len(li1) - 1):
        li1[i].next = li1[i + 1]

    for i in range(len(li2) - 1):
        li2[i].next = li2[i + 1]

    l1 = li1[0]
    l2 = li2[0]

    merged = solution.mergeTwoLists(l1, l2)

    while merged.next is not None:
        print(merged.val)
        merged = merged.next
