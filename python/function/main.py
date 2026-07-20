def cek_kelulusan(nilai : float) -> str :
    if nilai >= 75 :
        return "Lulus"
    else :
        return "Tidak Lulus"

print(cek_kelulusan(65.0))