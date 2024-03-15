## input
## x = int(input("masukkan jumlah:")) ## bil.bulat
## x = input("masukkan nama: ") ## string
## x = float(input("masukkan nilai:")) ## bil.real

## output
## print("4/3 = " + str(4/3) +".")

## Input,Output Tipe data
from operator import truediv
from types import TracebackType


print("----INPUT,OUTPUT TIPE DATA")

n = int(input("masukkan bilangan:")) ## Soal 1

digit1 = n // 10000
digit2 = (n // 1000) % 10
digit3 = (n // 100) % 10
digit4 = (n // 10) % 10
digit5 = n % 10

result = digit1 * digit2 * digit3 * digit4 * digit5
print("hasil perkalian: " + str(result))

print("masukkan jam sekarang") ## Soal 2

jam = int(input("masukkan jam: "))
menit = int(input("masukkan menit: "))
detik = int(input("masukkan detik: "))
durasi_timer_detik = int(input("masukkan X: "))

## jumlah detik dalam 1 hari = 24*60*60
waktu1 = (jam * 3600) + (menit * 60) + detik
waktu2 = (waktu1 * durasi_timer_detik) % (24 * 60 * 60)

jam2 = waktu2 // 3600
menit2 = (waktu2 % 3600) // 60
detik2 = waktu2 % 60

print("countdown akan berhenti pada jam: " + str(jam2) + ", menit " + str(menit2) + ", detik " + str(detik2))

## Percabangan (IF,ELIF,ELSE)
      print("----PERCABANGAN (IF,ELIF,ELSE")
    n = 5 
    if (n == 0):
    print("nol")
elif (n > 0):
    if (n % 2 == 0): ## % = modulus / sisa bagi
        print("positif genap")
    else:
        print("positif ganjil")
else:
    print("negatif")


## Perulangan (For loop,while)
print("----PERULANGAN (FOR LOOP,WHILE")

## Penggunaan for dengan list:
buah = ['tomat','melon','apel']
sayur = ['bayam','kangkung','sawi','kentang']
daftar_belanja = [buah,sayur]

for x in daftar_belanja:
    print(x)
    for komponen in x:
        print(komponen)

## Penggunaan for dengan range:
for i in range(10,40,2): 
## angka 2 merupakan perintah 
## agar angka yang keluar merupakan kelipatan 2
    print(i)

number = 50
for i in range(0,30):
    print(i)
    if i == number:
        print('number found',i)
        break  ## break fungsinya untuk keluar dari looping
else:
    print('tidak ada')
## Jika angka yang dimasukkan tidak ada dalam range
## maka break tidak akan berfungsi dan langsung
## masuk ke else.
## Sebaliknya,jika angka ada dalam range maka else
## tidak akan muncul


## Penggunaan While:
angka = 0

while angka < 5:
    print('angka adalah',angka)
    angka = angka + 1
else:
    print('angka terakhir adalah',angka)


start = True ## variabel boolean
angka = 5

while start:
    print('searching')
    if angka == 100:
        start = False ## variabel boolean
        print('i found the love')
    angka += 1 ## arti += 1 adalah semuanya akan ditambah 1

for i in range(1,6):
    for j in range(1, (i+1)):
        print(j)










