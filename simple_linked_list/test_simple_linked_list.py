from simple_linked_list import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(0)
    linked_list.push(3)
    current = linked_list.list_head
    
    while current:
        print(current.value())
        current = current.next_node
    
    linked_list.pop()
    current = linked_list.list_head
    while current:
        print(current.value())
        current = current.next_node
    print("lenght: ", len(linked_list))
    
if __name__ == "__main__":
    main()