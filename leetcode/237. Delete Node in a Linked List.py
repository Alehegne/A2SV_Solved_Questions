class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        # so the next node sacrificed and the current node takes its value and next pointer, effectively deleting the next node from the linked list.
