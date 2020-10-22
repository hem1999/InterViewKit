"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    cur = head
    slow = head
    fast = head
    if head==None or head.next==None or head.next.next==None:
        return False
        
    while(True):
        slow = slow.next
        fast = fast.next.next
        if fast==None or fast.next==None:
            return False
        if slow==fast:
            return True