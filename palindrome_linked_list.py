# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        slow = head
        stack = []
        ispalin = True

        while slow != None:
            stack.append(slow.val)
            slow = slow.next

        while head != None:
            i = stack.pop()
            if head.val == i:
                pass
            else:
                ispalin = False
                break
            head = head.next
        return ispalin
