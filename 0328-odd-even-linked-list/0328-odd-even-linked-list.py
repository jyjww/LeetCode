# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if head and head.next:
            even = head.next
            even_head = even

            while even and even.next:
                # odd 연결을 위해 even을 빼고 연결
                odd.next = even.next
                odd = odd.next

                # 빼둔 even을 서로 연결
                even.next = odd.next
                even = even.next
            # odd의 마지막과 even의 시작을 연결
            odd.next = even_head
        return head

        