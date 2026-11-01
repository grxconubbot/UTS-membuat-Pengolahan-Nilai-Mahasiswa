
def pengolahan_nilai():
    print("\n=== SISTEM PENGOLAHAN NILAI MAHASISWA ===")

    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    # Menghitung nilai akhir
    akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    # Menentukan nilai huruf
    if akhir >= 85:
        huruf = "A"
    elif akhir >= 80:
        huruf = "-A"
    elif akhir >= 75:
        huruf = "+B"
    elif akhir >= 70:
        huruf = "B"
    elif akhir >= 65:
        huruf = "-B"
    elif akhir >= 60:
        huruf = "+C"
    elif akhir >= 55:
        huruf = "C"
    elif akhir >= 50:
        huruf = "-C"
    elif akhir >= 47:
        huruf = "+D"
    elif akhir >= 44:
        huruf = "D"
    elif akhir >= 40:
        huruf = "-D"
    else:
        huruf = "E"

    # Menentukan status kelulusan
    if akhir >= 60 and uas >= 50:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    # Menampilkan hasil
    print("\n=== HASIL PENGOLAHAN NILAI ===")
    print(f"Nama mahasiswa : {nama}")
    print(f"Nilai akhir    : {akhir:.2f}")
    print(f"Nilai huruf    : {huruf}")
    print(f"Status         : {status}")


while True:
    pengolahan_nilai()

    ulang = input("\nInput mahasiswa lain? (y/n): ").lower()
    if ulang != "y":
        print("Program selesai.")
        break
