from typing import Any
import json

class APILuar:
    def kirim_data_mentah(self, endpoint: str, data: dict[str, Any]) -> str:
        return f"data terkirim ke {endpoint}: {json.dumps(data)}"

    def ambil_data_json(self, url: str) -> dict[str, Any]:
        return {"status": "oke", "data": [{"id": 1, "nama": "data katalog produk A"}]}

class APIDataWrapper:
    def __init__(self) -> None:
        self.__api_luar = APILuar()

    def tambah_produk(self, nama_produk: str, harga: int) -> str:
        data: dict = {
            "nama": nama_produk,
            "harga": harga,
            "kategori": "umum"
        }
        return self.__api_luar.kirim_data_mentah("/produk/tambah", data)

    def daftar_ingpo_produk(self) -> list[dict[str, Any]]:
        respon = self.__api_luar.ambil_data_json("/produk/semua")
        return respon.get("data", [])

if __name__ == "__main__":
    api_data = APIDataWrapper()

    tambah_produk_laptop = api_data.tambah_produk("laptop gaming warga slowy", 400_000)
    print(tambah_produk_laptop)

    data_list = api_data.daftar_ingpo_produk()
    print(data_list)

