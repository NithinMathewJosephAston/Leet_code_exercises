class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next

        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        list3 = []
        while newHead is not None:
            list3.append(newHead.val)
            newHead = newHead.next
        return list3


if __name__ == "__main__":
    l1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(3)
    l1.next = l1_2
    l1_2.next = l1_3

    l2 = ListNode(1)
    l2_2 = ListNode(2)
    l2_3 = ListNode(4)
    l2.next = l2_2
    l2_2.next = l2_3
    sol = Solution()
    print(sol.mergeTwoLists(l1, l2))


