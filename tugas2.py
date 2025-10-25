class SepedaMotor:
    # Class variables: dibagikan oleh semua instance
    total_motor = 0  # Menghitung total motor yang dibuat
    jenis = "Sepeda Motor"  # Atribut umum untuk semua motor

    def __init__(self, merk, model, cc, tahun, warna, surat):
        # Instance variables: unik untuk setiap objek
        self.merk = merk
        self.model = model
        self.cc = cc
        self.tahun = tahun
        self.warna = warna
        self.surat = surat
        
        # Increment class variable setiap kali instance baru dibuat
        SepedaMotor.total_motor += 1

    def tampilkan_info(self):
        print(f"Jenis: {SepedaMotor.jenis}")  # Mengakses class variable
        print(f"Motor: {self.merk} {self.model}")
        print(f"CC: {self.cc} | Tahun: {self.tahun} | Warna: {self.warna}")
        print(f"Surat yang dimiliki: {', '.join(self.surat)}")
        print("-" * 30)

    @classmethod
    def tampilkan_total_motor(cls):
        # Method class untuk menampilkan total motor (menggunakan class variable)
        print(f"Total {cls.jenis} yang dibuat: {cls.total_motor}")

# Membuat instance
motor1 = SepedaMotor(
    merk="Honda",
    model="Beat",
    cc="110",
    tahun="2022",
    warna="Merah",
    surat=["STNK", "BPKB", "Asuransi"]
)

motor2 = SepedaMotor(
    merk="Yamaha",
    model="Mio",
    cc="125",
    tahun="2021",
    warna="Hitam",
    surat=["STNK", "BPKB"]
)

# Menampilkan info dan total
print("Daftar Sepeda Motor:")
motor1.tampilkan_info()
motor2.tampilkan_info()
SepedaMotor.tampilkan_total_motor()  # Output: Total Sepeda Motor yang dibuat: 2
