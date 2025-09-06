
from typing import Protocol


class MetodePembayaran(Protocol):
    def bayar(self, jumlah: float) -> None:
        ...

class PembayaranTunai:
    def bayar(self, jumlah: float) -> None:
        print(f"bayar dengan tunai jumlah: Rp {jumlah:.0f}")

class PembarayanEwallet:
    def bayar(self, jumlah: float) -> None:
        print(f"bayar dengan ewallet: Rp {jumlah:.2f} (QR terbaca - saldo gass)")

class PembayaranKartu:
    def bayar(self, jumlah: float) -> None:
        print(f"bayar dengan kartu (otorisasi): Rp {jumlah} (berhasil...!)")


def proses_bayar(metode: MetodePembayaran, jumlah: float) -> None:
    metode.bayar(jumlah)

if __name__ == "__main__":
    tunai = PembayaranTunai()
    qr_code = PembarayanEwallet()
    kartu = PembayaranKartu()

    proses_bayar(tunai, 75_000)
    proses_bayar(qr_code, 550_000)
    proses_bayar(kartu, 1_200_000)
