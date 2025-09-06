# kelas = cetakan blueprint
# object = hasil dari desain

class Pelayan:
    def __init__(self, nama: str, umur: int, gaji: float) -> None:
        self.nama: str = nama
        self.umur: int = umur
        self.gaji: float = gaji
        self.pesanan_diantar: list[str] = []

    def ambil_pesanan(self, pesanan: str) -> None:
        print(f"{self.nama} mengambil pesanan pelaggan, info pesanan: {pesanan}")

    def antar_makanan(self, pesanan: str) -> None:
        self.pesanan_diantar.append(pesanan)
        print(f"{self.nama} mengantar {pesanan} ke meja pelanggan")
        self.cek_status()


    def cek_status(self) -> None:
        if len(self.pesanan_diantar) >= 5:
            self.status = "capek"
        else:
            self.status = "siap"
        print(f"status pelayan {self.nama}: {self.status}")

if __name__ == "__main__":
    pelayan_arfy = Pelayan("arfy", 25, 4_000_000)
    pelayan_nongpal = Pelayan("nongpal", 21, 5_500_000)

    pelayan_arfy.ambil_pesanan("nasi goreng")
    pelayan_nongpal.ambil_pesanan("mie goreng")

    pelayan_arfy.ambil_pesanan("es teh")
    pelayan_arfy.antar_makanan("nasi goreng")
    pelayan_arfy.antar_makanan("es teh")

    pelayan_nongpal.antar_makanan("mie goreng")
