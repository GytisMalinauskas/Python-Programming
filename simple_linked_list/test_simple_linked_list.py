from simple_linked_list import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    current = linked_list.list_head
    
    while current:
        print(current.value())
        current = current.next_node
    
if __name__ == "__main__":
    main()