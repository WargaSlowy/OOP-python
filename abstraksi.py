
from abc import ABC, abstractmethod


class Pembayaran(ABC):
    @abstractmethod
    def proses_pembayaran(self, jumlah: int) -> bool:
        pass

    def validasi_jumlah(self, jumlah: int) -> bool:
        return jumlah > 0

class PembayaranEwallet(Pembayaran):
    def proses_pembayaran(self, jumlah: int) -> bool:
        if not self.validasi_jumlah(jumlah):
            print("jumlah tidak valid!")
            return False
        
        print(f"respon pembayaran ewallet dengan total Rp.{jumlah}")
        return True

class PembayaranKartu(Pembayaran):
    def proses_pembayaran(self, jumlah: int) -> bool:
        if not self.validasi_jumlah(jumlah):
            print("jumlah tidak valid untuk kartu atm")
            return False
        
        print(f"respon pembayaran dengan kartu atm dengan total Rp.{jumlah}")
        print("pembayaran berhasil")
        return True


def bayar(pembayaran: Pembayaran, jumlah: int) -> None:
    pembayaran.proses_pembayaran(jumlah)


if __name__ == "__main__":
    ewallet = PembayaranEwallet()
    kartu_atm = PembayaranKartu()

    bayar(ewallet, 150_000) 
    bayar(kartu_atm, 230_000)
