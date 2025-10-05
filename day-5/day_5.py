# this will be doen in normal python
"""list1 = []
list2 = [0]

merged = sorted(list1 + list2)
print(merged)

"""

# Definition of a node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # value stored in this node
        self.next = next    # pointer to the next node (None if last)

# Solution class with merge function
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()       # Step 1: Create a dummy node to start the merged list
        tail = dummy             # Step 2: Tail points to last node in merged list (currently dummy)

        # Step 3: Traverse both lists until one ends
        while list1 and list2:
            if list1.val < list2.val:     # Compare the current nodes
                tail.next = list1         # Attach the smaller node to merged list
                list1 = list1.next       # Move forward in list1
            else:
                tail.next = list2         # Attach the smaller node from list2
                list2 = list2.next       # Move forward in list2
            tail = tail.next              # Move the tail to the new last node

        # Step 4: Attach the remaining nodes (if any list is not finished)
        tail.next = list1 or list2

        # Step 5: Return the merged list, skipping the dummy node
        return dummy.next
