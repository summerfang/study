#Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while head.next.next is not None:
            first = head
            second = head.next
            third = head.next.next
            
            head.next = head
            head = head.next


if __name__ == '__main__':
    solution = Solution()
    l4 = ListNode(val=4)
    l3 = ListNode(val=3, next=l4)
    l2 = ListNode(val=2, next=l3)
    l1 = ListNode(val=1, next=l2)

    h = l1
    while(h.next):
        print("{}{}".format(h.val," "), end="")
        h = h.next

    print(h.val)

    h = solution.reverseList(l1)

    while(h.next):
        print("{}{}".format(h.val," "), end="")
        h = h.next

    print(h.val)
    