#Menginput Nilai Nama, Prodi, Tugas, UTS, dan UAS
nama = (input("Masukkan Nama Mahasiswa: "))
prodi = (input("Masukkan Nama Prodi: "))
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
 
#Menghitung Nilai Akhir sesuai dengan Bobot
nilai =  (0.15 * tugas) + (0.35 * uts) +  (0.50 * uas)
 
#Menentukan Grade Berdasarkan Nilai Akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'
 
#Menentukan Status Kelulusan Berdasarkan Nilai Akhir
if nilai > 60:
    status = 'Lulus'
else:
    status = 'Tidak Lulus'

if status == 'Lulus':
    selamat ='Selamat Anda Lulus!!'
else:
    selamat = 'Selamat Mencoba Kembali. Semangat!!'
 
#Menampilkan Nilai Akhir, Grade, dan Status Kelulusan
print('Nama Mahasiswa: ', nama)
print('Nama Prodi: ', prodi)
print('Nilai Akhir: %0.2f' % nilai)
print('Grade: {}'.format(grade))
print('Status: {}'.format(status))
print(selamat)