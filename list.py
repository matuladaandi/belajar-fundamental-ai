# sifat list itu seperti halnya string pada file variabel.py
umur = [7,14,21,28]
# print(umur[2]) # 21
print(umur[-1])
print(umur[-3:])


# Semua operasi slice mengembalikan list baru yang berisi elemen yang diminta.
# Ini berarti bahwa slice berikut mengembalikan salinan dangkal (shallow copy) dari list tersebut:
rgb = ["red", "green", "blue"]
rgba = rgb
rgba.append("alph")
# print(rgba)

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5]= ['C','D','E']

print(letters)

# remove
letters[2:5] = []
print(letters)

letters[:] = []
print(letters)
print(len(letters))

# list bersarang
buah = ['apel', 'anggur', 'jeruk', 'semangka']
angka = [1,2,3,4,5,6,7,8,9,10]
x = [buah, angka]
print(x)
print(x[0]) #['apel', 'anggur', 'jeruk', 'semangka']
print(x[0][2]) #jeruk
