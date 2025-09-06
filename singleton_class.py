
from typing import ClassVar, Optional


class KonfigurasiApps:
    _instace: ClassVar[Optional["KonfigurasiApps"]] = None

    def __new__(cls) -> "KonfigurasiApps":
        if cls._instace is None:
            cls._instace = super().__new__(cls)
        return cls._instace

    def __init__(self) -> None:
        if not hasattr(self, "sudah_diinialisasi"):
            self.nama_aplikasi: str = "aplikasi WargaSlowy"
            self.versi: str = "1.0.0"
            self.mode_debug: bool = False
            self.database_url: str = "sqlite:///app.db"
            self.sudah_diinialisasi = True

    def tampilkan_konfigurasi(self) -> None:
        print(f"aplikasi: {self.nama_aplikasi}")
        print(f"ingpo aplikasi: {self.versi}")
        print(f"debug mode: {'aktif' if self.mode_debug else 'tidak aktif'}")
        print(f"database: {self.database_url}")

if __name__ == "__main__":
    konfig_pertama = KonfigurasiApps()
    konfig_kedua = KonfigurasiApps()
    
    konfig_pertama.tampilkan_konfigurasi()
    konfig_kedua.tampilkan_konfigurasi()

    konfig_pertama.mode_debug = True

    print(f"apakah sama: {konfig_pertama is konfig_kedua}")
