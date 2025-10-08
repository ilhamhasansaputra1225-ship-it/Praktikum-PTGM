while True:
    print("\n=== Kalkulator Sederhana ===")

    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == '+':
        print("Hasil:", angka1 + angka2)
    elif operator == '-':
        print("Hasil:", angka1 - angka2)
    elif operator == '*':
        print("Hasil:", angka1 * angka2)
    elif operator == '/':
        if angka2 == 0:
            print("Error: tidak bisa dibagi nol.")
        else:
            print("Hasil:", angka1 / angka2)
    else:
        print("Operator tidak dikenal.")

    ulang = input("Mau hitung lagi? (y/n): ")
    if ulang.lower() != 'y':
        break

print("Terima kasih sudah pakai kalkulator.")