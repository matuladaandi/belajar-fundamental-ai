nama = "andi"
petiksatu = 'contoh petik satu'
kalimatPanjang = """ ini contoh
kalimat panjang nya atau 
multy baris
"""
umur = 26
tinggi = 153.9

empty_string = ""
anothers_empty_string = ' '

print(nama)
print(umur)
print(type(tinggi))
print(type(nama))
print(petiksatu)
print(kalimatPanjang)

string_double = 'First Line. \nSecond Line.'

print(string_double)
print('c:\this\name')  # here \t means tab, \n means newline
print(r'c:\this\nameY') # note the r before the quote


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

mergeString = "ini " + "contoh " + "string " + "yang " + "di " + "gabungkan"
mergeString2 = 'ini ' 'contoh ' 'string ' 'yang ' 'di ' 'gabungkan' ' kedua'

print(mergeString)
print(mergeString2)

# string panjang yang akan dipecah
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

prefix = 'py'
print(prefix + 'thon')

word = 'python'
print(word[0])
print(word[5])
print('\n')
print(word[-1])
print(word[-6])