"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
from Node import Node, create_linked_list, output_as_list


def remove_dupes(head):
    """Removes all of the duplicate values in a linked list and returns
    the head.

    >>> output_as_list(remove_dupes(create_linked_list([1,1,1])))
    [1]

    >>> output_as_list(remove_dupes(create_linked_list([1,2,3,3,3])))
    [1, 2, 3]

    >>> output_as_list(remove_dupes(create_linked_list([1,1,4,5,5,5,6,7,7])))
    [1, 4, 5, 6, 7]

    >>> output_as_list(remove_dupes(create_linked_list([])))
    []
    """

    if not head:
        return None

    seen = set()
    current = head
    prev = None

    while current.next:
        if current.val not in seen:
            # Point the previous node to the current one if the
            # value has not been seen before.
            seen.add(current.val)
            if prev:
                prev.next = current
            prev = current

        current = current.next

    # If there are duplicates after the last number, point the last Node to None
    if current.val in seen:
        prev.next = None

    return head
