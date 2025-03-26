class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)  # Creation d'un nouveau node
        new_node.next = self.head  
        self.head = new_node  

    def insert_at_end(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # si la lise est vide on fait du nouveau node le head
            return
        last = self.head 
        while last.next:  # Sion, on parcours la liste jusqu'au dernier node
            last = last.next
        last.next = new_node  # le nouveau node devien le next du dernier node

    def print_list(self):
        temp = self.head # on commence par le head de la lise
        while temp:
            print(temp.data,end=' ') 
            temp = temp.next 
        print()  

    def delete_from_beginning(self):
        if self.head is None:
            return "The list is empty" # On retourne se texte si le node est vide
        self.head = self.head.next  # Sinon, sinon on suprime le head en mettant le prochain node comme head
    
    def delete_from_end(self):
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None  # Si il y a un seul node, on transforme le head en none
            return
        temp = self.head
        while temp.next.next:  # Sinon, on va au dernier node
            temp = temp.next
        temp.next = None  # On supprime le dernier node en metan non au pointeur nex de l'avant-dernier node


    def search(self, value):
        current = self.head  # Start with the head of the list
        position = 0  # compteur de position
        while current: # on parcours la liste
            if current.data == value: # commpare la daa actuel a la valeur
                return f"Value '{value}' found at position {position}" # on affiche quand la comparaison concorde
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list" 
    
    
if __name__ == '__main__':
    # Creation d'une instance
    llist = LinkedList()

    # Insertion au debut 
    llist.insert_at_beginning('fox') 
    llist.insert_at_beginning('brown') 
    llist.insert_at_beginning('quick')  
    llist.insert_at_beginning('the')  

    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

# Insert a word at the end
    llist.insert_at_end('jumps')

   # Print the list before deletion
    print("List before deletion:")
    llist.print_list()

    # Deleting nodes from beginning and end
    llist.delete_from_beginning()
    llist.delete_from_end()

    # Print the list after deletion
    print("List after deletion:")
    llist.print_list()
    
    print(llist.search('quick'))  
    # Print the list
    llist.print_list()