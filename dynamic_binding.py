from typing import Protocol


class SistemAlarm(Protocol):
    def aktifkan(self) -> None: ...


class AlarmDasar:
    def aktifkan(self) -> None:
        print("bunyi sirine")

class AlarmPinter:
    def aktifkan(self) -> None:
        print("kirim notifikasi bahaya ke smartphone")

class AlarmPihakBerwajib:
    def aktifkan(self) -> None:
        print("memanggil pihak berwajib")

class RumahPintar:
    def __init__(self, nama_pemilik: str) -> None:
        self.nama_pemilik: str = nama_pemilik
        self.alarm_terpasang: list[SistemAlarm] = []

    def pasang_alarm(self, alarm: SistemAlarm) -> None:
        self.alarm_terpasang.append(alarm)

    def picu_alarm(self) -> None:
        print(f"rumah {self.nama_pemilik} dalam marabahaya")
        for alarm in self.alarm_terpasang:
            alarm.aktifkan()

if __name__ == "__main__":
    rumah_arfy = RumahPintar("arfy slowy")

    rumah_arfy.pasang_alarm(AlarmDasar())
    rumah_arfy.pasang_alarm(AlarmPinter())
    rumah_arfy.pasang_alarm(AlarmPihakBerwajib())

    rumah_arfy.picu_alarm()
