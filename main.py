"""
menunjukkan semua syntaxes python
"""
from geometry.persegipanjang import hitung_luas_persegipanjang
from geometry.segitiga import hitung_luas_segitiga
from geometry_class.segitiga import Segitiga

print("Hello World")

# menghitung luas segi3

alas = 20
tinggi = 3
luas_segitiga = alas * tinggi
print(luas_segitiga)

# logika percabangan
if luas_segitiga < 30:
    print("kecil")
elif luas_segitiga == 30:
    print("cukupan")
else:
    print("buesar bgt")

# perulangan
print("Dengan for")
for i in range(0, 10):
    print(i+1, luas_segitiga)


# modularisasi 1 => fungsi
#
# print("Segitiga 1")
# alas = 20
# tinggi = 3
# luas_segitiga = alas * tinggi
# print(luas_segitiga)

print(hitung_luas_segitiga("Segitiga 1", 5, 15))
print(hitung_luas_segitiga("Segitiga 2", 3, 6))
print(hitung_luas_persegipanjang("Persegi Pjg 1", 10, 4))
print(hitung_luas_persegipanjang("Persegi Pjg 1", 11, 3))


# modularisasi tahap 3 => class

segitiga1 = Segitiga('Segitiga 1 as class', 30, 4)
print(segitiga1.hitung_luas())
segitiga2 = Segitiga('Segitiga 2 as class', 9, 2)
print(segitiga2.hitung_luas())