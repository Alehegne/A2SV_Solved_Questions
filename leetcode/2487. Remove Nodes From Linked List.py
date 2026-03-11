# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _reverse(self,head):
        prev = None
        curr = head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self._reverse(head)
        temp = head
        st = [temp.val] #preserve monot increasing,doesnt pop
        temp = temp.next
        while temp:
            if temp.val >= st[-1]:
                st.append(temp.val)
            temp = temp.next
        
        head = ListNode(st[-1])
        st.pop()
        temp = head
        while st:
            temp.next = ListNode(st.pop())
            temp = temp.next

        return head





        
