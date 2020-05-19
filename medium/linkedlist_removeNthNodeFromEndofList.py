from medium.add_two_numbers import ListNode


def remove_nth_node_from_end(head, n):
    """
    链表这种数据结构的特点和使用

    使用双指针

    使用一个dummyHead简化操作

    :param head:
    :param n:
    :return:
    """
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    for i in range(n):
        first = first.next

    while first.next:
        second = second.next
        first = first.next

    second.next = second.next.next

    return dummy.next


