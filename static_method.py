

import re
from typing import Final


class ValidasiPengguna:
    panjang_minimal_password: Final[int] = 8
    domain_perusahaan: Final[str] = "@WargaSlowy.com"

    def __init__(self, email: str, password: str) -> None:
        self.email: str = email
        self.password: str = password
        self.adalah_valid: bool = False

    def validasi_lengkap(self) -> bool:
        if not ValidasiPengguna.validasi_email(self.email):
            print("email enggak valid")
            return False
        if not ValidasiPengguna.validasi_password(self.password):
            print("password tidak mengandung huruf besar, dan juga angka")
            return False
        self.adalah_valid = True
        return True

    @staticmethod
    def validasi_email(email: str) -> bool:
        pola = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pola, email) is not None

    @staticmethod
    def validasi_password(password: str) -> bool:
        if len(password) < ValidasiPengguna.panjang_minimal_password:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        return True

if __name__ == "__main__":
    email = "arfyslowy@ringkih.com"
    password = "ArfySlowy6789"

    if ValidasiPengguna.validasi_email(email):
        print(f"email kamu benar")
    else:
        print(f"email kamu salah")

    if ValidasiPengguna.validasi_password(password):
        print(f"password kamu valid info password: {password}")
    else:
        print("password kamu tidak valid")
