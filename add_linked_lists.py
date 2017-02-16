# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head1 = l1
        head2 = l2
        op = ListNode(0)
        head3 = op
        while (head1 and head2):
            sum = head1.val + head2.val + carry
            if (sum < 10):
                carry = 0
            else:
                sum = sum % 10
                carry = 1
            op.val = sum
            head1 = head1.next
            head2 = head2.next
            if (head1 or head2):
                tmp = ListNode(None)
                op.next = tmp
                op = op.next
        while (head1):
            sum = head1.val + carry
            if (sum < 10):
                carry = 0
            else:
                sum = sum % 10
                carry = 1
            op.val = sum
            head1 = head1.next
            if (head1):
                tmp = ListNode(None)
                op.next = tmp
                op = op.next
        while (head2):
            sum = head2.val + carry
            if (sum < 10):
                carry = 0
            else:
                sum = sum % 10
                carry = 1
            op.val = sum
            head2 = head2.next
            if (head2):
                tmp = ListNode(None)
                op.next = tmp
                op = op.next
        if (carry):
            op.next = ListNode(1)

        return head3
