# class Parent
class MhsAlumni:
    def lulus(self):
        print("Anda sudah lulus")

    def ijazah(self):
        print("Anda memiliki ijazah kelulusan.")


class MhsAktif:
    def aktif(self):
        print("Anda mahasiswa aktif")

    def ktm(self):
        print("Anda memiliki Kartu Tanda Mahasiswa (KTM).")

    def beasiswa(self):
        print("Anda terdaftar sebagai penerima beasiswa.")


# class Child
class Bagus(MhsAlumni):
    pass


class Surya(MhsAktif):
    pass


class Dede(MhsAlumni, MhsAktif):
    pass



bagus = Bagus()
surya = Surya()
dede = Dede()


dede.ktm()
dede.ijazah()