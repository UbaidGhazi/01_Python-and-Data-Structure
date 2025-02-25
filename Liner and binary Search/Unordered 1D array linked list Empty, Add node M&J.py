class Node:
    def __init__(self, data, next_node=-1):
        self.data = data
        self.next_node = next_node
#(b) Write program code for the main program.
#Declare a 1D array of type node with the identifier linkedList, and initialise it with the data shown in the table on page 2. Declare the pointers.

linked_list = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6),
               Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]
start_pointer = 0
empty_list = 5

#(c) The procedure outputNodes() takes the array and startPointer as parameters.The procedure outputs the data from the linked list by following the nextNode values. 
#(i)Write program code for the procedure outputNodes().

def output_nodes(linked_list, current_pointer):
    while current_pointer != -1:
        print(linked_list[current_pointer].data)
        current_pointer = linked_list[current_pointer].next_node


def add_node(linked_list, current_pointer, empty_list):
    data_to_add = int(input("Enter the data to add: "))

    if empty_list < 0 or empty_list > 9:
        return False
    else:
        new_node = Node(data_to_add)
        linked_list[empty_list] = new_node

        previous_pointer = 0
        while current_pointer != -1:
            previous_pointer = current_pointer
            current_pointer = linked_list[current_pointer].next_node

        linked_list[previous_pointer].next_node = empty_list
        empty_list = linked_list[empty_list].next_node

        return True


linked_list = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6),
               Node(0, 7), Node(56, 3), Node(0, 9), Node(0, -1)]
start_pointer = 0
empty_list = 5
output_nodes(linked_list, start_pointer)
return_value = add_node(linked_list, start_pointer, empty_list)
if return_value:
    print("Item successfully added")
else:
    print("Item not added, list full")
output_nodes(linked_list, start_pointer)