# Stack Adalah Struktur Data Yang Menggunakan Konsep Last In First Out (LIFO) Artinya Elemen Terakhir Yang Masuk Adalah Pertama Yang Keluar
# Biasa Di Gunakan Untuk Menyimpan Data Yang Berurutan, seperti Stack Buku


# Stack Versi List class Stack

class Stack:
    def __init__(self) -> None:
        self.data : list[int] = []

    def is_empty(self) -> bool :
        return len(self.data) == 0

    def push(self, item : int) -> None:
       self.data.append(item) # -> .append maksudnya menambahkan elemen baru ke list di akhir

    def pop(self) -> int :
        return self.data.pop() # -> .pop maksudnya menghapus elemen terakhir dari list

    def peek(self) -> int :
        return self.data[-1] # -> .peek maksudnya melihat elemen terakhir dari list

    def size(self) -> int :
        return len(self.data) # -> .size maksudnya melihat jumlah elemen dari list


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"peek: {stack.peek()}")
    print(f"size: {stack.size()}")
    stack.pop()
    print(f"peek: {stack.peek()}")
    print(f"size: {stack.size()}")


