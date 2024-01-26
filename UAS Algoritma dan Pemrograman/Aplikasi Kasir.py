#Menginput nama, alamat, no telepon, dan tanggal 
print("--------------- Rumah Makan Dasi dan Kursi ----------------")
pembeli = input("Masukkan nama Pembeli: ")
alamat = input("Masukkan alamat rumah Pembeli: ")
No_telp = int(input("Masukkan No. Telepon Pembeli: "))
import time
hari_ini = time.asctime( time.localtime(time.time()) )
data = pembeli + "di" + alamat + "dengan nomer telepon:"  
print ("Pesanan atas nama :", pembeli) 

#memanggil fungsi 
def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
#menampilkan menu makanan
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 15000")
   print("2. Soto - Rp 9000")
   print("3. Mie Ayam - Rp 11000")
   print("4. Bakso - Rp 12000")
   print("5. Mie goreng - Rp 10000")
#menginput pilihan makanan serta porsi pelanggan
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))

#Menentukan pilihan makanan serta porsi pelanggan
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," porsi Soto = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   elif nomor==4:
       totalmkn=porsi*12000
       print (porsi," porsi Bakso = Rp", totalmkn)
       mkn=("Bakso")
   elif nomor==5:
       totalmkn=porsi*10000
       print (porsi," porsi Mie goreng = Rp", totalmkn)
       mkn=("Mie gorang")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

#memanggil funsgi
def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. Es kopi - Rp 4000")
   print("4. Es soda - Rp 5000")
   print("5. Air Es - Rp 1500")
#mengiinput pilihan minuman serta porsi pelanggan
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

#menentukan pilihan minuman serta porsi pelanggan
   if nomor==1:
       totalmnm=gelas*2000
       print (gelas," gelas Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
   elif nomor==4:
       totalmnm=gelas*5000
       print (gelas," gelas Es soda = Rp", totalmnm)
       mnm=("Es soda")
   elif nomor==5:
       totalmnm=gelas*1500
       print(gelas," gelas Air es = Rp", totalmnm)
       mnm=("Air Es")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

#mentotal semua harga makanan dan minuman
fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

#menampilkan total, uang pelanggan, dan kembaliannya
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

#menampilkan struk dari total pembelian
print("\n===================================")
print("======= S T R U K   B E L I =======")
print("===================================")
print ("Nama\t\t\t:",pembeli)
print ("Alamat\t\t\t:", alamat)
print ("Nomor Telepon\t\t:", "+62",No_telp)
print ("Beli\t\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Total\t\t\t: Rp",totalsemua)
print ("Dibayar\t\t\t: Rp",uang)
print ("Kembalian\t\t: Rp",kembalian)
print ("Tanggal pembelian\t:", hari_ini)
print("===================================")
print("===================================")
