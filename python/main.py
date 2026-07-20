
# variabel

nama_siswa : str = "Radian"
nilai_ujian : float = 90.5
status : bool = True    

# If else conditional

bmi: float = 22.5
status_bmi: str = ""

if bmi < 18.5 : 
    status_bmi = "Kurus"
elif bmi < 25 :
    status_bmi = "Normal"
elif bmi < 30 :
    status_bmi = "Kelebihan Berat Badan"
else :
    status_bmi = "Obesitas"

# Loop

total_nilai_ujian: list[float] = [80.0, 75.5, 90.0, 60.0]
total: float = 0.0

for nilai in total_nilai_ujian:
    total += nilai


angka : int = 10

while angka > 0 :
    print(angka)
    angka -= 1
print("Selesai")


