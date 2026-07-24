class Node :
    def __init__(self, data: str) -> None:
        self.data : str = data
        self.next : Node | None = None


class QueueLinkedList :
    def __init__(self) -> None:
        self.head : Node | None = None
        self.tail : Node | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, item: str) -> None:
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        assert self.tail is not None
        self.tail.next = new_node
        self.tail = new_node


    def dequeue(self) -> str | None :
        if self.is_empty():
            return None

        assert self.head is not None
        head_node : Node = self.head
        self.head = self.head.next
        
        if self.head is None :
            self.tail = None
            
        return head_node.data

    def peek(self) -> str | None :
        if self.is_empty():
            return None

        assert self.head is not None
        return self.head.data


if __name__ == "__main__":
    queue = QueueLinkedList()
    queue.enqueue("Budi")
 
    print(f"dequeue: {queue.dequeue()}")

    print(f"peek: {queue.peek()}")
    

    
    