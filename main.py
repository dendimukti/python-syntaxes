"""
menunjukkan semua syntaxes python
"""
from geometry.persegipanjang import hitung_luas_persegipanjang
from geometry.segitiga import hitung_luas_segitiga

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