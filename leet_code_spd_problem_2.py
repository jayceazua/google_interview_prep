# Leet Code SPD1.01 Problem 2
# Question: Add Two Numbers Linked List


# Restate: So, I have two non-empty linked lists. And the data containing the linked list are non-negative integers. In total they represent a number but it is reversed. So for example 3->2->1 is simply 123. With that I need to add these two numbers. Then I need to return the total of those two numbers as a reversed representation linked list. Also, besides each individual node, the total number of a linked list will not be zero?

# Clarifying Questions:
# 1. does the linked list have a tail property
# 2. Does the linked lists given have to be singly or can they be doubly
# 3. is the data in the linked data type of int or strings or both
# 4. what does "two numbers do not contain any leading zero, except the number 0 itself." mean?

# Assumptions:
# 1. the linked list has a head and tail properties
# 2. the linked list given have head and tail properties.
# 3. I can create my own node and linked list class

# Think out load

  # brainstorm solutions: I'm thinking about traversing through the given linked list and getting the values
  # from each node and putting it into a list and later reversing those numbers to get a single whole number.
  # Then repeating the same function for the second linked list and then adding them together.
  # With that given whole integer, I convert it into a string in order to traverse through the number.
  # I reverse traverse and start creating nodes of the inverse representation of the added number.

  # explain your rationale:

  # discuss trade offs:

  # suggest improvements:

# Leetcode:
