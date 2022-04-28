# Definition for singly-linked list.
from sqlalchemy import null


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            new_head = self.swapPairs(head.next.next)
            first = head
            second = head.next            
            head.next = new_head
            second.next = first
        return second


if __name__ == '__main__':
    solution = Solution()
    l4 = ListNode(val=4)
    l3 = ListNode(val=3, next=l4)
    l2 = ListNode(val=2, next=l3)
    l1 = ListNode(val=1, next=l2)

    h = l1
    while(h.next):
        print(h.val)
        h = h.next

    print(h.val)

    h = solution.swapPairs(l1)

    while(h.next):
        print(h.val)
        h = h.next

    print(h.val)
    