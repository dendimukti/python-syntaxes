"""
menunjukkan semua syntaxes python
"""
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

def hitung_luas_segitiga(title, alas, tinggi):
    print(title)
    return (alas * tinggi) / 2

print(hitung_luas_segitiga("Segitiga 1", 5, 15))
print(hitung_luas_segitiga("Segitiga 2", 3, 6))