# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_node = l1
        first = str(current_node.val)

        while current_node.next:
            first = str(current_node.next.val) + first
            current_node = current_node.next

        current_node = l2
        second = str(current_node.val)

        while current_node.next:
            second = str(current_node.next.val) + second
            current_node = current_node.next
        #print('test')
        #print(first)
        #print(second)
        ans = int(first) + int(second)
        #print(ans)
        
        current_node = ListNode(val=int(str(ans)[0]))

        for i in range(len(str(ans))-1):

            new_node = ListNode(val=int(str(ans)[(1+i)]))
            new_node.next = current_node
            current_node = new_node
        return current_node