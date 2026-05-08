try:
    angka = int(input("Masukkan Angka : "))
    print(f"Anda memasukkan: {angka}")
except ValueError: # Spesifik: hanya tangkap error konversi tipe
    print(f"Error: Input harus berupa bilangan bulat")
except Exception as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nProgram diberhentikan paksa oleh pengguna")
    raise SystemExit