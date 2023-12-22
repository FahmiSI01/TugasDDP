class Hewan:
    def __init__(self, nama, makanan, habitat, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembang_biak = berkembang_biak

    def info(self):
        print(f"Nama hewan: {self.nama}")
        print(f"Makanannya: {self.makanan}")
        print(f"Hidupnya: di {self.habitat}")
        print(f"Berkembang biak dengan cara: {self.berkembang_biak}")
        print("-------------------------------------")

class Badak(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "tumbuhan", habitat, "melahirkan")

class Ikan(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "plankton", habitat, "bertelur")

class Ular(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "daging", habitat, "bertelur")

# Penggunaan class di atas
badak_jawa = Badak("Badak Jawa", "Hutan")
ikan_nemo = Ikan("Ikan Nemo", "Laut")
ular_kobra = Ular("Ular Kobra", "Hutan")

badak_jawa.info()
ikan_nemo.info()
ular_kobra.info()