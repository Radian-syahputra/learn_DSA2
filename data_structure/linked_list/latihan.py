

class Node :
    def __init__(self, data : str) -> None:
        self.data : str = data
        self.next : Node | None = None


class LinkedList : 
    def __init__(self) -> None:
        self.head : Node | None = None

 
    def add(self, item: str) -> None:
        new_node : Node = Node(item)

        if(self.head is None) :
            self.head = new_node
            return

        current_node : Node = self.head
        while current_node.next is not None :
            current_node = current_node.next
        current_node.next  = new_node

    def print_list(self) -> None :
        if self.head is None :
            print("List Tidak Ada")
            return

        current_node : Node | None = self.head
        while current_node is not None :
            print(current_node.data)
            current_node = current_node.next
        print("None")


    def len_list(self) -> int :
        count : int = 0
        current_node : Node | None= self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count
    


# Catatan : Cari tahu kenapa    def isEmpty(self) : return self.head is None (Method) ini tidak bisa ditambahkan 
# harus pakai self.head is None
    
