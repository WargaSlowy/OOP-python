from typing import Any
import inspect


class Produk:
    def __init__(self, nama: str, harga: int) -> None:
        self.nama_produk: str = nama
        self.harga_produk: int = harga
        self.kategori: str = "umum"

    def tampilkan_info(self) -> None:
        print(f"produk: {self.nama_produk}")
        print(f"harga: Rp.{self.harga_produk}")
        print(f"kategori: {self.kategori}")

    def ubah_harga(self, harga_baru: int) -> None:
        if harga_baru > 0:
            self.harga_produk = harga_baru
            print(f"harga sekarang menjadi: Rp.{harga_baru}")
        else:
            print("harga baru tidak valid")


def analisis_objek(objek: Any) -> None:
    print(f"analisis objek: {type(objek).__name__}")

    print("attribut data:")
    for nama, nilai in inspect.getmembers(objek):
        if not nama.startswith("_"):
            if not callable(nilai):
                print(f"{nama}: {nilai}")

    metode: list[str] = []
    for nama, metode_obj in inspect.getmembers(objek, predicate=inspect.ismethod):
        if not nama.startswith("_"):
            metode.append(nama)
            print(f"-{nama}")

    if "tampilkan_info" in metode:
        print("memanggil tampilkan_info() secara dinamis:")
        metode_tampilkan = getattr(objek, "tampilkan_info")
        metode_tampilkan()


if __name__ == "__main__":
    produk_data = Produk("laptop warga slowy", 400_000)

    analisis_objek(produk_data)
    #
    # setattr(produk_data, "harga_produk", 30_000)
    # print(f"harga baru: Rp.{getattr(produk_data, 'harga_produk')}")
