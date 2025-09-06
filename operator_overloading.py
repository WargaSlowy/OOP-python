# kotak A = 3 apel
# kotak B = 5 jeruk

class Toko:
    def __init__(self, nama: str, produk: list[str]) -> None:
        self.nama: str = nama
        self.produk: list[str] = produk

    def __add__(self, toko_lain: "Toko") -> "Toko":
        nama_baru = f"{self.nama} {toko_lain.nama}"
        produk_gabungan = self.produk + toko_lain.produk
        return Toko(nama = nama_baru, produk = produk_gabungan)

    def __eq__(self, lain: "Toko") -> bool:
        return self.produk == lain.produk

    def __str__(self) -> str:
        daftar = ", ".join(self.produk) if self.produk else "kosong"
        return f"Toko {self.nama} (produk: {daftar})"

if __name__ == "__main__":
    toko_elektronik = Toko("wargaslowy tech", ["laptop", "mouse", "keyboard"])
    toko_buku = Toko("wargaSlowy baca", ["buku komputer", "tutorial gajah 3000 jam", "cara jadi rek"])

    toko_baru = toko_elektronik + toko_buku

    print(toko_baru)
