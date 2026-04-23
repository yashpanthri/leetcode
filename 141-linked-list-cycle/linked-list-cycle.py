# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        bool = False
        start = head
        while( not start is None):
            if start in sett:
                bool = True
                break
            else:
                sett.add(start)
                start = start.next

        return bool