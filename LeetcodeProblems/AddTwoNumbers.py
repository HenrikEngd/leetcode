# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = Solution()
        sum = solution.helper1(l1) + solution.helper1(l2)
        return solution.helper2(sum)
    
    def helper1(self,l1: Optional[ListNode]) -> int:
        tmplist = []
        print(l1.val, l1.next)
        while(l1.next != None):
            tmplist.append(l1.val)
            l1 = l1.next
        tmplist.append(l1.val)
        tmplist.reverse()
        int_result = int(''.join(map(str, tmplist)))
        return int_result
    
    def helper2(self, numb: int) -> Optional[ListNode]:
        numblist = [int(x) for x in str(numb)]
        numblist.reverse()
        print(numblist)
        current = tmp = ListNode(0)
        for x in numblist:
            current.next = ListNode(x)
            current = current.next
        return tmp.next