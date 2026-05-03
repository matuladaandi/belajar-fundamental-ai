x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

umur = int(input("Please enter your age: "))
if umur >= 18:
    print("You age is ",umur,"old" " Welcome to Game")
elif umur < 18:
    print("You age is",umur,"old" " You are not allowed to play")

def klasifikasi_nilai(nilai : float) -> str:
    """
    Mengembalikan kelasifikasi nilai akademik menjadi grade

    arg :
        Nilai : Angka antara 0-100

    return:
        String grade (A, B, C, D, E)
    """
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return  "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"

# Test
test_values = [90.5, 80, 70, 60, 50]
for test in test_values:
    hasil = klasifikasi_nilai(test)
    print(f"Nilai {test}: Grade {hasil}")