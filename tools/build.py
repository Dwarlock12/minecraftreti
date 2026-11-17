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
                if ".b64" in name:
                    continue
                full = os.path.join(root, name)
                rel = os.path.relpath(full, src_dir)
                info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                with open(full, "rb") as f:
                    z.writestr(info, f.read())


def main():
    os.makedirs(DIST, exist_ok=True)
    zip_dir(BP_DIR, BP_PACK)
    zip_dir(RP_DIR, RP_PACK)
    with zipfile.ZipFile(ADDON, "w", zipfile.ZIP_DEFLATED) as z:
        for pack in (BP_PACK, RP_PACK):
            info = zipfile.ZipInfo(os.path.basename(pack), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            with open(pack, "rb") as f:
                z.writestr(info, f.read())
    for path in (BP_PACK, RP_PACK, ADDON):
        print(f"{path} ({os.path.getsize(path)} octets)")


if __name__ == "__main__":
    main()
