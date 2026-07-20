class Siswa : 
    def __init__(self, name : str, nilai_ujian: float) -> None:
        self.name = name
        self.nilai_ujian = nilai_ujian

    def cek_kelulusan(self) -> str :
        if self.nilai_ujian >= 75 :
            return "Lulus"
        else :
            return "Tidak Lulus"

# Penjelasan 
# Siswa Adalah Nama Class yang merepresentasikan siswa
# name, nilai_ujian adalah atribut yang merepresentasikan nama dan nilai ujian siswa
# cek_kelulusan adalah method yang mengecek apakah siswa lulus atau tidak
# radian adalah objek dari class Siswa


if __name__ == "__main__":
    radian = Siswa("Radian", 73.5)
    christy = Siswa("Christy", 80.0)    
    print(radian.cek_kelulusan())
    print(christy.cek_kelulusan())
