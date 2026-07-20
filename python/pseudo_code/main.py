
def cari_nilai_terendah(daftar_nilai: list[int]) -> int :
    terendah: int = daftar_nilai[0]
    for nilai in daftar_nilai :
        if nilai < terendah :
            terendah = nilai
    return terendah


daftar_nilai = [10, 5, 8, 3, 7]
print(cari_nilai_terendah(daftar_nilai))

