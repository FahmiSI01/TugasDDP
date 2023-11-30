
# Jawaban Soal NO 1
print("===============================================================================================================================")
def lulus_saja(hasil_akhir):
    siswa_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]
    return siswa_lulus

# Buat fungsi untuk membuat list baru berisi daftar nama siswa yang lulus
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]
def daftar_nama_siswa():
    daftar_siswa=[]
    for siswa in hasil_akhir:
        daftar_siswa.append(siswa.get('nama'))
    return [siswa.get('nama')]

hasil_lulus = lulus_saja(hasil_akhir)
print("Nama-Nama Siswa yang lulus:", hasil_lulus)

# Jawaban Soal NO 2
print("===============================================================================================================================")
def balikan(buah_buahan):
    buah_terbalik = []
    for buah in buah_buahan[::-1]:
        buah_terbalik.append(buah)
    return buah_terbalik

# Buat fungsi untuk membuat list baru berisi daftar urutan buah buahan yang dibalik
hasil_terbalik = balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
print("Urutan terbalik buah-buahan:", hasil_terbalik)


# Jawaban Soal NO 3
print("===============================================================================================================================")
def duplikasi(buah_buahan):
    buah_diduplikasi = []
    for buah in buah_buahan:
        buah_diduplikasi.append(buah)
        buah_diduplikasi.append(buah)
    return buah_diduplikasi

# Buat fungsi untuk membuat list baru berisi daftar buah-buahan yang diduplikasi
hasil_duplikasi = duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
print("List buah dengan duplikasi:", hasil_duplikasi)

# Jawaban Soal NO 4
print("===============================================================================================================================")
def hanya_konsonan(kalimat):
    konsonan = ""
    for karakter in kalimat:
        if karakter.isalpha() and karakter.lower() not in 'aeiou':
            konsonan += karakter
    return konsonan

# Buat fungsi untuk membuat string berisi hanya konsonan
hasil_konsonan = hanya_konsonan("Nurul Fikri")
print("Huruf Konsonan dari string yaitu:", hasil_konsonan)
print("===============================================================================================================================")

