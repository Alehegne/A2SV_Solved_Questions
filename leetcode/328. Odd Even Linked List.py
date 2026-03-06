# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def tra(self,head):
        t = head
        while t:
            print(t.val,end="->")
            t = t.next
        print()
        
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # odd = ListNode(head.val)
        # even = ListNode(head.next.val)
        # temp = head.next.next
        # n = 1
        # temp_o = odd
        # temp_e = even
        # while temp:
        #     if not n % 2:
        #         temp_e.next = ListNode(temp.val)
        #         temp_e = temp_e.next
        #     else:
        #         temp_o.next = ListNode(temp.val)
        #         temp_o = temp_o.next
        #     temp = temp.next
        #     n += 1
        # temp_o.next = even
        # return odd
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = even_head
        return head






        
