class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        carry, val = divmod(val, 10)
        current.next = ListNode(val)
        current = current.next

    if carry == 1:
        current.next = ListNode(1)

    return dummy.next
