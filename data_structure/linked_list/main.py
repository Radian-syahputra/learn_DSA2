class Node : 
    def __init__(self, data : int) -> None:
        self.data : int  = data
        self.next: Node | None = None 

class LinkedList :
    def __init__(self) -> None:
        self.head: Node | None = None 

    
    def tambah_node_sampai_akhir(self, data: int) -> None:
        node_baru : Node = Node(data)

        if(self.head is None) :
            self.head = node_baru
            return

        node_sekarang : Node = self.head # -> Node Awal
        while node_sekarang.next is not None:
            node_sekarang = node_sekarang.next # -> Node Akhir
        node_sekarang.next = node_baru

    def tambah_node_di_awal(self, data: int) -> Node :
        node_baru : Node = Node(data)
        node_baru.next = self.head
        self.head = node_baru
        return node_baru
    
    def tampilkan_jumlah_node(self) -> int: 
        node_sekarang : Node | None = self.head
        count: int = 0
        while node_sekarang is not None:
            count += 1
            node_sekarang = node_sekarang.next
        return count


    def print_list(self) -> None :
        node_sekarang: Node | None = self.head
        while node_sekarang is not None :
            print(node_sekarang.data, end=" -> ")
            node_sekarang = node_sekarang.next
        print("None")