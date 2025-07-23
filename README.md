# README.md

# Singly Linked List Implementation

This project contains a Python implementation of a singly linked list. The linked list supports various operations such as appending, prepending, removing, and reversing nodes. 

## Features

- **Append**: Add a node to the end of the list.
- **Prepend**: Add a node to the beginning of the list.
- **Pop**: Remove the last node from the list.
- **Pop First**: Remove the first node from the list.
- **Get**: Retrieve a node by its index.
- **Set Value**: Update the value of a node at a specific index.
- **Insert**: Insert a node at a specific index.
- **Remove**: Remove a node from a specific index.
- **Reverse**: Reverse the order of the nodes in the list.

## Usage

To use the linked list implementation, you can create an instance of the `LinkedList` class and call its methods. Below is an example of how to use the linked list:

```python
from main import LinkedList

# Create a new linked list
my_linked_list = LinkedList(1)

# Append nodes
my_linked_list.append(2)
my_linked_list.append(3)

# Prepend a node
my_linked_list.prepend(0)

# Print the list
print('Current Linked List:')
my_linked_list.print_list()

# Remove the last node
my_linked_list.pop()

# Print the list after popping
print('Linked List after popping the last node:')
my_linked_list.print_list()

# Reverse the linked list
my_linked_list.reverse()

# Print the reversed list
print('Reversed Linked List:')
my_linked_list.print_list()
```

## Installation

To run this project, you need Python installed on your machine. Clone the repository and run the `main.py` file to see the linked list in action.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
