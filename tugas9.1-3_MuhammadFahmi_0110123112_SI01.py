# Jawaban No 1 membuat fungsi data diri
print("===================================================================")
def profile(nama, alamat, gender, umur, hobi):
    print("nama saya adalah : ", nama)
    print("saya tinggal di : ", alamat)
    print("jenis kelamin saya : ", gender)
    print("saya berumur : ", umur)
    print("Hobi saya yaitu: ", hobi)

profile("Muhammad Fahmi", "Bogor", "Laki-laki", "19 Tahun", "Bermain alat kesenian")

# Jawaban NO 2 Membuat Fungsi Kelulusan 
print("===================================================================")
def kelulusan(nilai):
    if nilai >= 0 and nilai <= 60:
        return "Gagal"
    elif nilai <= 70:
        return "Baik"
    elif nilai <= 80:
        return "Sangat Baik"
    elif nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai Tidak Valid!"

print("Status kelulusan anda : ",kelulusan(82))

# Jawaban No 3 Membuat fungsi nilai bilangan ganjil dari prameter
print("===================================================================")
def bilangan_ganjil(bilangan):
    for i in range(bilangan):
        if i % 2 != 0:
            print(i)

bilangan_ganjil(100)
print("===================================================================")
