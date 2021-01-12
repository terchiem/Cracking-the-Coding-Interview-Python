class Node:
    """Single node class."""

    def __init__(self, val=None):
        self.val = val
        self.next = None


def create_linked_list(arr):
    """Creates a linked list from an array and returns the head."""
    result = []
    head = Node()
    current = head

    for n in arr:
        current.next = Node(n)
        current = current.next

    return head.next


def output_as_list(head):
    """Outputs a linked list as a list."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result
