# mencari data ganjil & genap
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for angka in data:
    if angka % 2 == 0:
        print(f" Ketemu Genap {angka}")
        break # jika ada satu & yang paling pertama angka genap maka akan berhenti

else:  # Perhatikan: else ini milik 'for', BUKAN milik 'if'!
    print( "Tidak ada bilangan dalam list yakni angka 1-10")