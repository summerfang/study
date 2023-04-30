# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        original_head = head

        len_of_node = 1

        while head.next:
            len_of_node += 1
            head = head.next

        head = original_head


        num_iter = len_of_node / 2

        for i in range(0, num_iter):
            head = head.next

        return head


if __name__ == "__main__":
    s = Solution()
    print(s.middleNode.val)