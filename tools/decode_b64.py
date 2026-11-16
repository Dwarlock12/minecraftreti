import base64
import glob
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = [
    "dist/Potions-de-Taille.mcaddon",
    "dist/PotionsTaille_BP.mcpack",
    "dist/PotionsTaille_RP.mcpack",
]


def main():
    for rel in FILES:
        parts = sorted(glob.glob(os.path.join(BASE, rel + ".b64.part*")))
        if not parts:
            raise FileNotFoundError(rel + ".b64.part*")
        b64 = "".join(open(p, "r", encoding="ascii").read().strip() for p in parts)
        data = base64.b64decode(b64)
        with open(os.path.join(BASE, rel), "wb") as f:
            f.write(data)
        print("decode:", rel, len(data), "octets depuis", len(parts), "parties")
    print("Termine. Double-cliquez sur dist/Potions-de-Taille.mcaddon pour installer.")
    print("(Les icônes PNG de src/ se régénèrent avec: python3 tools/make_textures.py)")


if __name__ == "__main__":
    main()
