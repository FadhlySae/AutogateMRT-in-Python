from __future__ import annotations

def render_arrow(direction: str) -> str:
    # Descriptoin: Build an ASCII arrow to show In or Out at the autogate.
    # Input: "in" for downward arrow, "out" for upward arrow.
    # Output: A multi-line string representing the arrow.

    if direction not in {"in", "out"}:
        raise ValueError("direction must be 'in' or 'out'")

    # ARROW IN
    if direction == "in":
        maxchar = 16
        maxbar = 5
        spasi = 10
        tinggi = 14
        panah = []

        for i in range(tinggi):
            # Menambahkan spasi sebelum bar
            panah.append(" " * min(spasi, 6) + "|||||")
            
            if i == 5:
                panah[i] = "\\\\    |||||    //"
                spasi = 3
            elif i > 5 and spasi >= 0:
                panah[i] = " " * (4 - spasi) + "\\\\" + " " * spasi + "|||||" + " " * spasi + "//"
                spasi  -= 1
            elif spasi == -1:
                spasi2 = 5
                panah[i] = " " * spasi2 + "\\\\|||//"
                spasi2 += 1
                spasi -= 1
            elif spasi < -1:
                panah[i] = " " * spasi2 + "\\\\|//"
                spasi2 += 1

        # settle last line (fix: wrong indexing)
        panah[-1] = ""
        panah[-2] = " " * (spasi2 - 2) + "\\|/"
        panahakhir = ["      |||||"]

        for i in panah:
            panahakhir.append(i)

        for i in panahakhir:
            print(i)

    # ARROW OUT (same steps)
    else:
        maxchar = 16
        maxbar = 5
        space = 10
        line = 14
        panah = []

        for i in range(line):
            
            panah.append(" " * min(space, 6) + "|||||")
            
            if i == 5:
                panah[i] = "//    |||||    \\\\"
                space = 3
            elif i > 5 and space >= 0:
                panah[i] = " " * (4 - space) + "//" + " " * space + "|||||" + " " * space + "\\\\"
                space -= 1
            elif space == -1:
                space2 = 5
                panah[i] = " " * space2 + "//|||\\\\"
                space2 += 1
                space -= 1
            elif space < -1:
                panah[i] = " " * space2 + "//|\\\\"
                space2 += 1

        
        panah[-1] = ""
        panah[-2] = " " * (space2 - 2) + "/|\\"
        panahakhir = ["      |||||"]

        for i in reversed (panah):
            panahakhir.append(i)

        
        for i in panahakhir:
            print(i)
