class Penyihir:
    def lempar_mantra(self) -> None:
        print("melempar mantra: reducto!")

class Petarung:
    def serang(self) -> None:
        print("menyerang dengan kekuatan pedang ksatria ngawi")


class PenyihirPetarung(Penyihir, Petarung):
    def gunakan_kekuatan_multi(self) -> None:
        self.lempar_mantra()
        self.serang()
        print("kombinasi double: lempar serangan khas boyolali")

if __name__ == "__main__":
    hero_rusdi = PenyihirPetarung()

    # hero_rusdi.lempar_mantra()
    # hero_rusdi.serang()
    # hero_rusdi.gunakan_kekuatan_multi()
    print(PenyihirPetarung.__mro__)
