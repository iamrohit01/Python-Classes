class Node:
    def __init__(self, value):
        """
        Initializes a new node with the given value.
        Args:
            value: The value to be stored in the node.
        """
        self.value = value  # Assign the provided value to the node
        self.next = None   # Initialize the next pointer to None

class LinkedList:
    def __init__(self, value):
        """
        Initializes a new linked list with a first node containing the given value.
        Args:
            value: The value to be stored in the first node of the linked list.
        """
        new_node = Node(value)  # Create a new node with the given value
        self.head = new_node     # Set the head of the list to the new node
        self.tail = new_node     # Set the tail of the list to the new node
        self.length = 1          # Initialize the length of the list to 1

    def print_list(self):
        """
        Prints the value of each node in the linked list, starting from the head.
        """
        temp = self.head         # Start at the head of the list
        while temp is not None:  # Iterate until the end of the list
            print(temp.value)    # Print the value of the current node
            temp = temp.next     # Move to the next node
        
    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.
        Args:
            value: The value to be stored in the new node.
        Returns:
            True: If the append operation was successful.
        """
        new_node = Node(value)  # Create a new node with the given value
        if self.length == 0:   # If the list is empty
            self.head = new_node  # Set both head and tail to the new node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Add the new node to the end of the list
            self.tail = new_node       # Update the tail to the new node
        self.length += 1           # Increment the length of the list
        return True                # Return True to indicate success

    def pop(self):
        """
        Removes the last node from the linked list.
        Returns:
            The removed node, or None if the list is empty.
        """
        if self.length == 0:      # If the list is empty
            return None             # Return None
        temp = self.head          # Start at the head
        pre = self.head           # Also keep track of the node before the last
        while(temp.next):         # Iterate until the last node
            pre = temp             # pre follows temp
            temp = temp.next      # temp moves to the next node
        self.tail = pre          # Update the tail to the node before the last
        self.tail.next = None     # Remove the last node
        self.length -= 1          # Decrement the length
        if self.length == 0:      # If the list is now empty
            self.head = None       # Set head to None
            self.tail = None       # Set tail to None
        return temp              # Return the removed node

    def prepend(self, value):
        """
        Adds a new node with the given value to the beginning of the linked list.
        Args:
            value: The value to be stored in the new node.
        Returns:
            True: If the prepend operation was successful.
        """
        new_node = Node(value)  # Create a new node
        if self.length == 0:   # If the list is empty
            self.head = new_node  # Set both head and tail to the new node
            self.tail = new_node
        else:
            new_node.next = self.head  # Point the new node to the current head
            self.head = new_node       # Update the head to the new node
        self.length += 1           # Increment the length
        return True                # Return True to indicate success

    def pop_first(self):
        """
        Removes the first node from the linked list.
        Returns:
            The removed node, or None if the list is empty.
        """
        if self.length == 0:      # If the list is empty
            return None             # Return None
        temp = self.head          # Store the current head
        self.head = self.head.next  # Move head to the next node
        temp.next = None          # Remove the original head's reference to the list
        self.length -= 1          # Decrement the length
        if self.length == 0:      # If the list is now empty
            self.tail = None       # Set tail to None
        return temp              # Return the removed node

    def get(self, index):
        """
        Gets the node at the specified index.
        Args:
            index: The index of the node to retrieve.
        Returns:
            The node at the specified index, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.length:  # If the index is invalid
            return None                         # Return None
        temp = self.head                      # Start at the head
        for _ in range(index):                # Iterate to the desired index
            temp = temp.next                  # Move to the next node
        return temp                          # Return the node at the index
        
    def set_value(self, index, value):
        """
        Sets the value of the node at the specified index.
        Args:
            index: The index of the node to modify.
            value: The new value for the node.
        Returns:
            True: If the value was successfully set.
            False: If the index is out of bounds.
        """
        temp = self.get(index)  # Get the node at the index
        if temp:               # If the node exists
            temp.value = value  # Set the new value
            return True         # Return True
        return False            # Return False if the node doesn't exist
    
    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index.
        Args:
            index: The index at which to insert the new node.
            value: The value of the new node.
        Returns:
            True: If the insertion was successful.
            False: If the index is out of bounds.
        """
        if index < 0 or index > self.length:  # If the index is invalid
            return False                        # Return False
        if index == 0:                         # If inserting at the beginning
            return self.prepend(value)          # Use prepend
        if index == self.length:                # If inserting at the end
            return self.append(value)           # Use append
        new_node = Node(value)               # Create a new node
        temp = self.get(index - 1)            # Get the node before the index
        new_node.next = temp.next             # Point the new node to the next node
        temp.next = new_node                  # Point the previous node to the new node
        self.length += 1                      # Increment the length
        return True                            # Return True

    def remove(self, index):
        """
        Removes the node at the specified index.
        Args:
            index: The index of the node to remove.
        Returns:
            The removed node, or None if the index is out of bounds.
        """
        if index < 0 or index >= self.length:  # If the index is invalid
            return None                         # Return None
        if index == 0:                         # If removing the first node
            return self.pop_first()             # Use pop_first
        if index == self.length - 1:            # If removing the last node
            return self.pop()                   # Use pop
        pre = self.get(index - 1)             # Get the node before the index
        temp = pre.next                      # The node to be removed
        pre.next = temp.next                  # Skip over the node to be removed
        temp.next = None                      # Remove the node's reference to the list
        self.length -= 1                      # Decrement the length
        return temp                          # Return the removed node

    def reverse(self):
        """
        Reverses the order of the nodes in the linked list.
        """
        temp = self.head                      # Start at the head
        self.head = self.tail                  # Swap head and tail
        self.tail = temp
        after = temp.next                    # Node after temp
        before = None                        # Node before temp
        for _ in range(self.length):          # Iterate through the list
            after = temp.next                  # Store the next node
            temp.next = before                 # Reverse the direction of the pointer
            before = temp                      # Move 'before' to the current node
            temp = after                       # Move 'temp' to the next node
  
# Example usage:
my_linked_list = LinkedList(1)  # Create a new linked list with value 1
my_linked_list.append(2)        # Append value 2
my_linked_list.append(3)        # Append value 3
my_linked_list.append(4)        # Append value 4

print('LL before reverse():')
my_linked_list.print_list()     # Print the list

my_linked_list.reverse()        # Reverse the list

print('\nLL after reverse():')
my_linked_list.print_list()


