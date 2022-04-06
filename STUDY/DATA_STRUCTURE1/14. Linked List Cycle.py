# 링크드 리스트를 이해하는 정도만 하자
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        stack=[]
        while head :
            if head.next in stack: return True
            stack.append(head)
            head=head.next
        return False