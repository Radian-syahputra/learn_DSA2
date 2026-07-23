# Stack Versi Linked List


class Node:
    def __init__(self, data: int) -> None:
        self.data : int = data
        self.next : Node | None = None

class Stack :
    def __init__(self) -> None:
        self.top : Node | None = None

    def isEmpty(self) -> bool :
        return self.top is None

    def push(self, data: int) -> None :
        new_node : Node | None = Node(data)

        if (self.isEmpty()) :
            self.top = new_node 

        new_node.next =  self.top
        self.top = new_node

    def pop(self) -> int | None :
        if(self.isEmpty()) :
            return None

        assert self.top is not None  # meyakinkan type checker
        top_node : Node | None = self.top
        self.top = self.top.next
        return top_node.data

    def peek(self) -> int | None :
        if self.isEmpty() :
            return None
            
        assert self.top is not None
        return self.top.data