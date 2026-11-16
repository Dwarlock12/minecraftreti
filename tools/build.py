import os
import zipfile

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "src")
DIST = os.path.join(BASE, "dist")

BP_DIR = os.path.join(SRC, "PotionsTaille_BP")
RP_DIR = os.path.join(SRC, "PotionsTaille_RP")
BP_PACK = os.path.join(DIST, "PotionsTaille_BP.mcpack")
RP_PACK = os.path.join(DIST, "PotionsTaille_RP.mcpack")
ADDON = os.path.join(DIST, "Potions-de-Taille.mcaddon")


def zip_dir(src_dir, out_path):
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(src_dir):
            dirs.sort()
            for name in sorted(files):
                if name.endswith(".b64"):
                    continue
                full = os.path.join(root, name)
                rel = os.path.relpath(full, src_dir)
                z.write(full, rel)


def main():
    os.makedirs(DIST, exist_ok=True)
    zip_dir(BP_DIR, BP_PACK)
    zip_dir(RP_DIR, RP_PACK)
    with zipfile.ZipFile(ADDON, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(BP_PACK, os.path.basename(BP_PACK))
        z.write(RP_PACK, os.path.basename(RP_PACK))
    for path in (BP_PACK, RP_PACK, ADDON):
        print(f"{path} ({os.path.getsize(path)} octets)")


if __name__ == "__main__":
    main()
