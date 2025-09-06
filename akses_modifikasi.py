

# public: nama_atribut
# protected: _nama_attribut
# private: __nama_atribut

class RekeningBank:
    def __init__(self, nomor_rekening: str, nama_nasabah: str, saldo_awal: float, pin: str) -> None:
        self.nomor_rekening: str = nomor_rekening
        self.nama_nasabah: str = nama_nasabah

        self._riwayat_transaksi: list[str] = []
        self._status_aktif: bool = True

        self.__saldo: float = saldo_awal
        self.__pin: str = pin

    def cek_saldo(self, pin: str) -> float:
        if not self.__verifikasi_pin(pin):
            print("pin salah akses kita tolak")
        return self.__saldo

    def __verifikasi_pin(self, pin_input: str) -> bool:
        return pin_input == self.__pin

if
