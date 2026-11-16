import base64
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = [
    "dist/Potions-de-Taille.mcaddon",
    "dist/PotionsTaille_BP.mcpack",
    "dist/PotionsTaille_RP.mcpack",
    "src/PotionsTaille_BP/pack_icon.png",
    "src/PotionsTaille_RP/pack_icon.png",
    "src/PotionsTaille_RP/textures/items/shrink_potion.png",
    "src/PotionsTaille_RP/textures/items/reset_potion.png",
]


def main():
    for rel in FILES:
        b64_path = os.path.join(BASE, rel + ".b64")
        with open(b64_path, "r", encoding="ascii") as f:
            data = base64.b64decode(f.read())
        with open(os.path.join(BASE, rel), "wb") as f:
            f.write(data)
        print("decode:", rel, len(data), "octets")
    print("Termine. Double-cliquez sur dist/Potions-de-Taille.mcaddon pour installer.")


if __name__ == "__main__":
    main()
