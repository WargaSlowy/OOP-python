class Kendaraan:
    def __init__(self, merek: str, kecepatan_maks: int) -> None:
        self.merek: str = merek
        self.kecepatan_maks: int = kecepatan_maks
        self._sedang_berjalan: bool = False

    def mulai(self) -> None:
        self._sedang_berjalan = True
        print(f"{self.merek} telah dinyalakan")

    def berhenti(self) -> None:
        self._sedang_berjalan = False
        print(f"{self.merek} berhenti")

class Mobil(Kendaraan):
    def __init__(self, merek: str, kecepatan_maks: int, jumlah_pintu: int) -> None:
        super().__init__(merek, kecepatan_maks)
        self.jumlah_pintu: int = jumlah_pintu

    def klakson(self) -> None:
        print(f"{self.merek} membunyikan klakson: aduh gantengnya")

class Motor(Kendaraan):
    def __init__(self, merek: str, kecepatan_maks: int, jenis_helm: str) -> None:
        super().__init__(merek, kecepatan_maks)
        self.jenis_helm: str = jenis_helm

    def wheelie(self) -> None:
        if self._sedang_berjalan:
            print(f"{self.merek} melakukan wheelie")
        else:
            print("nyalakan dahulu dari si motornya")

if __name__ == "__main__":
    mobil = Mobil("toyota", 180, 4)
    motor = Motor("honda", 120, "full face")

    mobil.mulai()
    mobil.klakson()
    mobil.berhenti()

    motor.wheelie()
