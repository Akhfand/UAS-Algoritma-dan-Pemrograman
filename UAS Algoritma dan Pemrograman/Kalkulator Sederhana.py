print ("Selamat datang di Kalkulator sederhana")
#input angka pertama dari user
angka1 = float(input("Masukkan angka pertama: "))

#menampilkan pilihan operasi matematika
print("Pilih operasi Matematika yang akan di gunakkan!")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

#input pilihan operasi dari user
operasi = input("Pilih operasi matematika: ")

#input angka kedua dari user
angka2 = float(input("Masukkan angka kedua: "))

#menampilkan hasil dari pilihan dan angka yang di input user 
if operasi == '1' :
    hasil = angka1 + angka2
    print("Hasil penjumlahan dari", angka1, "+", angka2, "adalah", hasil)
elif operasi == '2' :
    hasil = angka1 - angka2
    print("Hasil pengurangan dari", angka1, "-", angka2, "adalah", hasil)
elif operasi == '3' :
    hasil = angka1 * angka2
    print("Hasil perkalian dari", angka1, "x", angka2, "adalah", hasil)
elif operasi == '4' :
    hasil = angka1 / angka2
    print("Hasil pembagian dari", angka1, ":", angka2, "adalah", hasil)
else :
    print("operasi yang kamu input invalid")

