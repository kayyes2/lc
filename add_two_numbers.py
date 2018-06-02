# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        times = 1
        total = 0
        carry = 0
        total_list = []
        if l1 and l2:
            # hint: check for is not None because l1.val would be false if the value is 0
            # hint: in fact l1.val is not necessary if none check is not necessary
            while (l1 and l1.val is not None) or (l2 and l2.val is not None):
                l1val = 0
                l2val = 0

                if l1 and l1.val:
                    l1val = l1.val

                if l2 and l2.val:
                    l2val = l2.val

                # total = total + (l1val + l2val)*times
                total = l1val + l2val + carry
                
                if total < 10:
                    carry = 0
                    total_list.append(total)
                else:
                    carry = 1
                    total_list.append(total-10)

                #times = times*10
                
                # hint: moe inside the other if
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
                    
            # hint: remember to add carry
            if carry:
                total_list.append(carry)
                
            return total_list
        else:
            raise Exception('not implemented')
