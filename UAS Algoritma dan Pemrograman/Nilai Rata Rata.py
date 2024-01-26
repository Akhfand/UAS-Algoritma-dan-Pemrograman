#input nama dan kelas 
nama = input("Masukkan nama mahasiswa: ")
kelas = input("Masukkan nama prodi: ")

#input jumlah tugas yang ada
def hitung_rata_rata_nilai():
    jumlah_nilai = int(input("Masukkan jumlah nilai tugas yang ada: "))
    nilai_list = []

#input nilai sesuai jumlah yang ada
    for i in range(jumlah_nilai):
        nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
        nilai_list.append(nilai)

#menampilkan nilai rata rata dari jumlah
    rata_rata = sum(nilai_list) / len(nilai_list)
    print(f"Rata-rata nilai: {rata_rata}")

#menampilkan nilai tertinggi dan terendah
    nilai_tertinggi = max(nilai_list)
    nilai_terendah = min(nilai_list)
    print(f"Nilai tertinggi: {nilai_tertinggi}")
    print(f"Nilai terendah: {nilai_terendah}")

#menampilkan hasil dari jumlahh rata rata nilai
    if rata_rata < 60 :
        print("Mohon maaf, Anda tidak lulus.")
    elif rata_rata == 60 :
        print("Nilai Anda memenuhi kategori Lulus. Namun tingkatkan kembali")
    else :
        print("Selamat Anda telah berhasil Lulus.")

if __name__ == "__main__":
    hitung_rata_rata_nilai()
