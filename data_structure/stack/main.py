# Contoh Implementasi Stack Versi List

class Stack :
    def __init__(self) -> None:
        self.data : list[int] = []

    def isEmpty(self) -> bool :
        if len(self.data) == 0 :
            return True
        return False

    def push(self, item: int) -> None:
        self.data.append(item)

    def pop(self) -> int :
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def peek(self) -> int :
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.data[-1]


class Undo :
    def __init__(self) -> None:
        self.data : list[str] = []

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def push(self, item : str) -> None :
        self.data.append(item)

    def pop(self) -> str :
        if self.isEmpty():
            raise IndexError("pop from empty undo stack")
        return self.data.pop()

    def peek(self) -> str :
        if self.isEmpty():
            raise IndexError("peek from empty undo stack")
        return self.data[-1]



if __name__ == "__main__":
    # 1. Buat objek Undo baru
    riwayat: Undo = Undo()
    
    # 2. push 3 aksi berturut-turut
    riwayat.push("ketik A")
    riwayat.push("ketik B")
    riwayat.push("hapus huruf")
    
    # 3. pop dua kali, tampilkan hasilnya
    aksi_di_undo_1 = riwayat.pop()
    # print(f"aksi_di_undo_1: {aksi_di_undo_1}")
    
    aksi_di_undo_2 = riwayat.pop()
    # print(f"aksi_di_undo_2: {aksi_di_undo_2}")
    
    # 4. tampilkan sisa aksi paling atas pakai peek()
    print(f"peek: {riwayat.peek()}")