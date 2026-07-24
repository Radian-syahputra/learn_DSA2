
# Queue Naif Versi List
class QueueNaif :
    def __init__(self):
        self.data : list[int] = []

    def is_empty(self) -> bool :
        return len(self.data) == 0

    def enqueue(self, item: int) -> None :
        return self.data.append(item)

    def dequeue(self) -> int | None :
        if self.is_empty() :
            return None

        return self.data.pop(0)


    def peek(self) -> int | None : # hanya menampilkan data terdepan
        if self.is_empty() :
            return None
        return self.data[0]

    def peek_all(self) -> list[int] :
        return self.data


# Queue Naif Versi LinkedList


class Node :
    def __init__(self, data : int) -> None:
        self.data : int = data
        self.next : Node | None = None


class QueueLinkedList :
    def __init__(self) -> None:
        self.head : Node | None = None
        self.tail : Node | None = None


    def is_empty(self) -> bool :
        return self.head is None

    def enqueue(self, item: int) -> int | None :
        new_node : Node = Node(item)
        
        if(self.is_empty()) :
            self.head = new_node
            self.tail = new_node
            
        assert self.tail is not None
        self.tail.next = new_node # self.tail.next = new_node, maksudnya menyambungkan si node terakhir SAAT INI ke node baru
        self.tail = new_node

    def dequeue(self) -> int | None :
        if self.is_empty() :
            return None

        assert self.head is not None
        first_node : Node = self.head
        self.head = first_node.next

        if self.head is None :
            self.tail = None
        return first_node.data

    
    