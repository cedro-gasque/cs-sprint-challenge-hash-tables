"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.prev = prev
        self.key = key
        self.value = value
        self.next = next

    def set_prev(self, value=None):
        self.prev = value
        return self

    def set_next(self, value=None):
        self.next = value
        return self

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = self.tail = node
        self.length = 0 + (node is not None)

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, key, value):
        head = self.head
        node = ListNode(key, value, prev=None, next=head)
        if head is None:
            self.tail = node
        else:
            head.prev = node
        self.head = node
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        head = self.head
        if head is self.tail:
            self.head = self.tail = None
        else:
            self.head = head.next.set_prev()
        self.length -= self.length > 0
        return head.value
    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, key, value):
        tail = self.tail
        node = ListNode(key, value, prev=tail, next=None)
        if tail is None:
            self.head = node
        else:
            tail.next = node
        self.tail = node
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tail = self.tail
        if tail is self.head:
            self.tail = self.head = None
        else:
            self.tail = tail.prev.set_next()
        self.length -= self.length > 0
        return tail.value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # this is dumb I admit but I can't help it
        # I just love writing nigh unreadable code
        if not node is self.head:
            if node is self.tail:
                self.tail = node.prev.set_next()
            else:
                node.prev.set_next(node.next).next.set_prev(node.prev)
            self.head = node.set_prev().set_next(self.head).next.set_prev(node).prev


    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not node is self.tail:
            if node is self.head:
                self.head = node.next.set_prev()
            else:
                node.next.set_prev(node.prev).prev.set_next(node.next)
            self.tail = node.set_next().set_prev(self.tail).prev.set_next(node).next

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is None:
            return node
        if node is self.head and node is self.tail:
            self.head = self.tail = None
        elif node is self.head:
            self.head = node.next.set_prev()
        elif node is self.tail:
            self.tail = node.prev.set_next()
        else:
            node.next.set_prev(node.prev).prev.set_next(node.next)
        self.length -= self.length > 0
        return node

    """
    Finds and returns the node with the specified key.
    """
    def get(self, key):
        current = self.head
        while current:
            if current.key == key:
                break
            current = current.next
        return current

    def to_list(self):
        output = []
        current = self.head
        while current:
            output.append((current.key, current.value))
            current = current.next
        return output

    def __repr__(self):
        string = "{"
        current = self.head
        while current:
            string += f"{current.key}: {current.value},\n"
            current = current.next
        return string + "}"
