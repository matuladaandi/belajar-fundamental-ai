# loop melalui list
fruits = ['apel', 'anggur', 'jeruk', 'semangka']
for fruit in fruits:
    print(f"saya suka {fruit}")

# Loop dengan indeks (pakai enumerate)
for index, fruit in enumerate(fruits):
    print(f"indeks ke-{index + 1} saya suka : {fruit}")

# Loop melalui string (string adalah iterable!)
for char in "Hello World":
    print(char)