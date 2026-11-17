# minecraftreti — Potions de Taille (Minecraft Bedrock addon)

Ready-to-install Bedrock addon (Windows 10) that lets the player shrink their
character by drinking potions, in steps: 100% → 80% → 60% → 40% → 20%, then
back to 100%. A second potion restores normal size (100%) directly.

- **Install:** download this repo (**Code → Download ZIP**, unzip), double-click `tools\build.bat` (Windows, PowerShell only, no Python needed) to build the `.mcaddon`/`.mcpack` from the text sources, then double-click `dist/Potions-de-Taille.mcaddon` and enable the packs in your world settings.
- **French install guide:** [README_FR.md](README_FR.md)
- **Sources:** `src/PotionsTaille_BP` (behavior pack: custom items + script using stable `@minecraft/server` 1.17.0, `minecraft:scale`) and `src/PotionsTaille_RP` (resource pack: 16×16 PNG icons + fr/en texts).
- **Rebuild fully from text:** `python3 tools/make_textures.py && python3 tools/build.py`, or on Windows simply `tools\build.bat` (PowerShell, no Python): the repo is 100% text, the 2 item icons are embedded as base64 in `tools/build.ps1` and the archives are rebuilt with .NET `ZipFile`.

No experimental features required. Works on Bedrock ≥ 1.21.0. The size change
is visual (player model scale via `minecraft:scale`): in first-person view you
cannot see your own body, so switch to third person (F5) or be watched by
another player to see it. The hitbox does not change (Bedrock limitation).
The `.mcaddon` embeds both packs; the two `.mcpack` files are also provided separately under `dist/`.
