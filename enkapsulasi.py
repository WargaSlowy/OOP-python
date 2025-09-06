from datetime import datetime
from typing import Optional

class RekeningBank:
    def __init__(self, nama_nasabah: str, saldo_awal: int, pin: str) -> None:
        self.__nama_nasabah: str = nama_nasabah
        self.__saldo: int = saldo_awal
        self.__pin: str = pin

        self._riyawat_transaksi: list = []

    def cek_saldo(self, pin: str) -> Optional[int]:
        if self.__verifikasi_pin(pin):
            return self.__saldo
        print("pin salah")
        return None

    def setor_tunai(self, jumlah: int) -> None:
        if jumlah <= 0:
            print("jumlah tidak valid")
            return
        self.__saldo += jumlah
        self._tambah_riyawat(f"setor -> +Rp {jumlah}")
        print(f"setor tunai Rp.{jumlah} berhasil!")

    def tarik_tunai(self, jumlah: int, pin: str) -> bool:
        if not self.__verifikasi_pin(pin):
            print("pin salah!")
            return False
        if jumlah <= 0 or jumlah > self.__saldo:
            print("jumlah tidak valid atau saldo tidak cukup")
            return False

        self.__saldo -= jumlah
        self._tambah_riyawat(f"Tarik tunai: -Rp {jumlah}")
        print(f"tarik tunai Rp.{jumlah} berhasil!")
        return True

    def __verifikasi_pin(self, pin_input: str) -> bool:
        return pin_input == self.__pin

    def _tambah_riyawat(self, transaksi: str) -> None:
        waktu = datetime.now().strftime("%H:%M")
        self._riyawat_transaksi.append(f"[{waktu} - {transaksi}]")

if __name__ == "__main__":
    rekening = RekeningBank("arfy slowy", 12_000_000, "23456789")

    rekening.setor_tunai(1_000_000)
    rekening.tarik_tunai(1_500_000, "23456789")

    print(f"sisa saldo: Rp.{rekening.cek_saldo("23456789")}")

    print(rekening.__saldo)
    rekening.__saldo = 9999999999
