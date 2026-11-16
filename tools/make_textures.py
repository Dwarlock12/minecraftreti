import os
import struct
import zlib

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RP_ITEMS = os.path.join(BASE, "src", "PotionsTaille_RP", "textures", "items")
BP_ICON = os.path.join(BASE, "src", "PotionsTaille_BP", "pack_icon.png")
RP_ICON = os.path.join(BASE, "src", "PotionsTaille_RP", "pack_icon.png")

BASE_PALETTE = {
    ".": (0, 0, 0, 0),
    "#": (43, 43, 43, 255),
    "g": (198, 228, 255, 190),
    "w": (255, 255, 255, 230),
}
SHRINK_PALETTE = dict(BASE_PALETTE, l=(36, 116, 255, 255), a=(12, 64, 190, 255))
RESET_PALETTE = dict(BASE_PALETTE, l=(52, 205, 80, 255), a=(22, 140, 45, 255))


def bottle_art(liquid_inner_rows):
    art = [
        "................",
        "......####......",
        "......#gg#......",
        "......#gg#......",
        "......#gg#......",
        ".....##gg##.....",
        "....#gggggg#....",
        "...#gggggggg#...",
        "...#wggggggg#...",
    ]
    for inner in liquid_inner_rows:
        assert len(inner) == 8, inner
        art.append("...#" + inner + "#...")
    art.append("...##########...")
    for line in art:
        assert len(line) == 16, (line, len(line))
    assert len(art) == 16
    return art


SHRINK_ART = bottle_art([
    "g" + "l" * 7,
    "l" * 8,
    "lll" + "aa" + "lll",
    "l" + "a" * 6 + "l",
    "lll" + "aa" + "lll",
    "l" * 8,
])

RESET_ART = bottle_art([
    "g" + "l" * 7,
    "lll" + "aa" + "lll",
    "l" + "a" * 6 + "l",
    "lll" + "aa" + "lll",
    "l" * 8,
    "l" * 8,
])


def write_png(path, rows):
    height = len(rows)
    width = len(rows[0])
    raw = b"".join(
        b"\x00" + b"".join(struct.pack("4B", *px) for px in row) for row in rows
    )

    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
    with open(path, "wb") as f:
        f.write(png)


def art_to_rows(art, palette):
    return [[palette[c] for c in line] for line in art]


def upscale(rows, factor):
    out = []
    for row in rows:
        wide = []
        for px in row:
            wide.extend([px] * factor)
        for _ in range(factor):
            out.append(list(wide))
    return out


def main():
    os.makedirs(RP_ITEMS, exist_ok=True)
    write_png(os.path.join(RP_ITEMS, "shrink_potion.png"), art_to_rows(SHRINK_ART, SHRINK_PALETTE))
    write_png(os.path.join(RP_ITEMS, "reset_potion.png"), art_to_rows(RESET_ART, RESET_PALETTE))
    icon_rows = upscale(art_to_rows(SHRINK_ART, SHRINK_PALETTE), 16)
    write_png(BP_ICON, icon_rows)
    write_png(RP_ICON, icon_rows)
    print("textures generees: shrink_potion.png, reset_potion.png, pack_icon.png (x2)")


if __name__ == "__main__":
    main()
