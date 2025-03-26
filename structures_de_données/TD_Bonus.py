class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insertion au début de la liste
    def insert_at_beginning(self, new_data):
        new_node = DoubleNode(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insertion à la fin de la liste
    def insert_at_end(self, new_data):
        new_node = DoubleNode(new_data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # Affichage de la liste
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    # Suppression au début de la liste
    def delete_from_beginning(self):
        if self.head is None:
            return "The list is empty"
        if self.head.next is None:  # Only one element in the list
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    # Suppression à la fin de la liste
    def delete_from_end(self):
        if self.tail is None:
            return "The list is empty"
        if self.tail.prev is None:  # Only one element in the list
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    # Recherche d'un élément dans la liste
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f"Value '{value}' found at position {position}"
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list"
    
if __name__ == '__main__':
    # Création d'une instance
    dllist = DoublyLinkedList()

    # Insertion au début
    dllist.insert_at_beginning('fox') 
    dllist.insert_at_beginning('brown') 
    dllist.insert_at_beginning('quick')  
    dllist.insert_at_beginning('the')  

    # Insertion à la fin
    dllist.insert_at_end('jumps')

    # Affichage de la liste
    print("Doubly Linked List:")
    dllist.print_list()

    # Suppression du début et de la fin
    dllist.delete_from_beginning()
    dllist.delete_from_end()

    # Affichage après suppression
    print("List after deletion:")
    dllist.print_list()
    
    print(dllist.search('quick'))  # Recherche d'un élément
    dllist.print_list()  # Affichage final de la liste
