# minecraftreti — Potions de Taille (Minecraft Bedrock addon)

Ready-to-install Bedrock addon (Windows 10) that lets the player shrink their
character by drinking potions, in steps: 100% → 80% → 60% → 40% → 20%, then
back to 100%. A second potion restores normal size (100%) directly.

- **Install:** download this repo (**Code → Download ZIP**, unzip), double-click `tools\decode_b64.bat` (Windows, no Python needed) or run `python3 tools/decode_b64.py` to rebuild the binary archives from the `.b64.partNN` chunks, then double-click `dist/Potions-de-Taille.mcaddon` and enable the packs in your world settings.
- **French install guide:** [README_FR.md](README_FR.md)
- **Sources:** `src/PotionsTaille_BP` (behavior pack: custom items + script using stable `@minecraft/server` 1.17.0, `minecraft:scale`) and `src/PotionsTaille_RP` (resource pack: 16×16 PNG icons + fr/en texts).
- **Rebuild fully from text:** `python3 tools/make_textures.py && python3 tools/build.py` (regenerates the PNG icons, then the `.mcpack`/`.mcaddon`).

No experimental features required. Works on Bedrock ≥ 1.21.0. The size change
is visual (player model scale). The `.mcaddon` embeds both packs; the two
`.mcpack` files are also provided separately under `dist/`.
