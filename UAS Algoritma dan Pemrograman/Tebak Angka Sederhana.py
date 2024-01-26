#import angka acak
import random

#menampilkan ucapan selamat datang dan pengenalan
def main():
    print("Selamat datang di Game Tebak Angka!")
    print("Saya telah memilih angka antara 1 dan 100.")
    print("Anda memiliki 5 kesempatan untuk menebak angka tersebut.")

#memasukkan angka rahasia, tebakan, dan kesempatan yang tersedia
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    kesempatan = 5

#menampilkan hasil pilihan dari player
    while tebakan != angka_rahasia and kesempatan > 0:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
        except ValueError: #angka yang dimasukkan tidak valid atau tidak sesuai
            print("Tolong masukkan angka yang valid.")
            continue

        if tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah.") #menampilkan hasil tebakan terlalu rendah
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi.") #menampilkan hasil tebakan terlalu tinggi
        else:
            print(f"Selamat! Anda berhasil menebak angka rahasianya: {angka_rahasia}") #menampilkan hasil tebakan yang benar

        kesempatan -= 1
        if kesempatan > 0 and tebakan != angka_rahasia:
            print(f"Anda memiliki {kesempatan} kesempatan lagi.") #menampilkan sisa kesempatan player yang tersedia

    if tebakan != angka_rahasia: #player kehabisan kesempatan dan tidak berhasil menebak
        print(f"Sayang sekali, Anda gagal menebak angka rahasianya. Angka rahasianya adalah {angka_rahasia}.")


if __name__ == "__main__":
    main()