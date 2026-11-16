# minecraftreti — Potions de Taille (Minecraft Bedrock addon)

Ready-to-install Bedrock addon (Windows 10) that lets the player shrink their
character by drinking potions, in steps: 100% → 80% → 60% → 40% → 20%, then
back to 100%. A second potion restores normal size (100%) directly.

- **Install file:** [dist/Potions-de-Taille.mcaddon](dist/Potions-de-Taille.mcaddon) — double-click it, then enable the packs in your world settings.
- **French install guide:** [README_FR.md](README_FR.md)
- **Sources:** `src/PotionsTaille_BP` (behavior pack: custom items + script using stable `@minecraft/server` 1.17.0, `minecraft:scale`) and `src/PotionsTaille_RP` (resource pack: 16×16 PNG icons + fr/en texts).
- **Rebuild:** `python3 tools/make_textures.py && python3 tools/build.py`

No experimental features required. Works on Bedrock ≥ 1.21.0. The size change
is visual (player model scale).
