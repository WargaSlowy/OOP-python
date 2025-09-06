
class Smartphone:
    def __init__(self, merek: str, model: str) -> None:
        self.merek: str = merek
        self.model: str = model
        self.baterai: int = 100

        self.__prossesor = self.__Prosesor()

    def nyalakan(self) -> None:
        if self.baterai > 10:
            print(f"hidupkan {self.merek} {self.model}")
            self.__prossesor.jalankan_simulasi()
        else:
            print("lowbat, mohon isi baterainya")

    def ingpo_smartphone(self) -> None:
        print(f"merek: {self.merek}")
        print(f"model: {self.model}")
        print(f"baterai ingpo: {self.baterai} %")
        print("prossor info:")
        self.__prossesor.tampilin_info()


    class __Prosesor:
        def __init__(self) -> None:
            self.nama = "snapslowy 8 gen 20"
            self.inti_cpu: int = 70
            self.kecepatan_ghz: float = 400.20

        def jalankan_simulasi(self) -> None:
            print(f"menjalankan sistem dengan {self.nama}")

        def tampilin_info(self) -> None:
            print(f"ingpo chip: {self.nama}")
            print(f"core cpu: {self.inti_cpu}")
            print(f"kecepatan: {self.kecepatan_ghz} GHz")

if __name__ == "__main__":
    hp_kita = Smartphone("slowy", "WargaSlowy G662")

    # hp_kita.ingpo_smartphone()
    hp_kita.nyalakan()

    prossesor = Smartphone.__Prosesor()
