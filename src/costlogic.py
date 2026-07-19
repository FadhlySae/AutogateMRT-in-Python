from __future__ import annotations


def build_fares(num_stations: int = 7, step_fare: int = 3000) -> list[int]:
    # Description: Build cumulative fares (tariff) per train station with multiples of 3000, fare increases by 3000 per station up to 7 entries.
    # Input: int (1-7)
    # Output: A list where index i stores the fare for station (i + 1).

    fares: list[int] = []
    total = 0
    for _ in range(num_stations):
        total += step_fare
        fares.append(total)
    return fares
