from __future__ import annotations

from .display import render_arrow
from .costlogic import build_fares


# MODULAR PROGRAM: Command Line Interface (cli.py)
# Description: Manage interactions with users by Terminal Command--Main Logic.
# Input: options A or B, and integer for credits/saldo.
# Output: Fail/Succes

def normalize_payment(raw: str) -> str:
    """Normalize payment input into 'QRIS' or 'TICKET'."""
    value = raw.strip().upper()
    if value in {"A", "QRIS"}:
        return "QRIS"
    if value in {"B", "TICKET"}:
        return "TICKET"
    else:
        print("Payment must be A/QRIS or B/TICKET")
        
    raise ValueError("Payment must be A/QRIS or B/TICKET")


def tap_in() -> int | None:
    """Simulate Tap-In. Returns saldo if using ticket; otherwise None."""
    render_arrow("in")
    print("==================")
    payment = normalize_payment(input("Payment (A=QRIS, B=Ticket): "))

    if payment == "QRIS":
        print("Scan the barcode with QRIS")
        print("==================")
        render_arrow("out")
        print("TRANSACTION SUCCES\nPLEASE ENTER")
        return None

    saldo = int(input("Masukkan saldo yang ingin di top-up: "))
    print("Tap Your Card")
    print("==================")
    render_arrow("out")
    print("TRANSACTION SUCCES\nPLEASE ENTER")
    return saldo


def tap_out(saldo: int | None, fares: list[int]) -> None:
    # Simulate Tap-Out using either QRIS or stored ticket balance
    render_arrow("in")
    print("==================")
    payment = normalize_payment(input("Payment (A=QRIS, B=Ticket): "))

    if payment == "QRIS":
        print("Scan the barcode with QRIS")
        render_arrow("out")
        print("==================")
        print("THANK YOU!")
        return

    if saldo is None:
        raise ValueError("Ticket tap-out requires saldo from tap-in.")

    tujuan = int(input("Choose your stations (1-7): "))
    if not (1 <= tujuan <= len(fares)):
        raise ValueError("Station is out of range.")

    fare = fares[tujuan - 1]
    if fare > saldo:
        print("Card Credit is not enough. Please Top-Up")
        return

    render_arrow("out")
    print("==================")
    print("THANK YOU!")
    print("Credits left:", saldo - fare)


def main() -> None:
    # fungsi utama sesuai alur proyek tubes
    fares = build_fares(num_stations=7, step_fare=3000)
    saldo = tap_in()
    tap_out(saldo, fares)


if __name__ == "__main__":
    main()
