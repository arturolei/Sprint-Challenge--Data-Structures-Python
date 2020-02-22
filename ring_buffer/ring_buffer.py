from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        # I assume "capacity" is the buffer limit
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            #If we have got room in our storage (below capacity), add without worry
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity:
            #If we are at capacity, we need to remove our head
            stash = self.storage.head #store for exceptional case at the end
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            
            #What if the head is the most "current thing"
            if stash == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        list_buffer_contents.append(self.current.value)

        if self.current.next is not None:
            #If the current node isn't the only value, let's move onto the next node
            next_node = self.current.next
        else:
            #If current node is only node, let's set next_node equal 
            #to the head to break from while loop condition (use next_node as flag)
            next_node = self.storage.head

        while next_node != self.current:
            #Traverse the list and add the new node to the array
            list_buffer_contents.append(next_node.value)

            if next_node.next is not None: #If we are not at the end, continue,
                next_node = next_node.next
            else:
                next_node = self.storage.head #If we are at the end, set to break loop condition

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
