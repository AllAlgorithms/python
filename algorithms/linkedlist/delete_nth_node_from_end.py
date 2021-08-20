# remove nth node from end
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# brute
# create a new linked list without that element
# Time O(n)
# Space O(n)

# optimal


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if(head.next == None):
            return None
        start = ListNode()
        start.next = head
        slow = fast = start
        for i in range(1, n+1):
            fast = fast.next
        while(fast.next != None):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return start.next
