@echo off
cd /d "%~dp0.."
for %%F in ("dist\Potions-de-Taille.mcaddon" "dist\PotionsTaille_BP.mcpack" "dist\PotionsTaille_RP.mcpack" "src\PotionsTaille_BP\pack_icon.png" "src\PotionsTaille_RP\pack_icon.png" "src\PotionsTaille_RP\textures\items\shrink_potion.png" "src\PotionsTaille_RP\textures\items\reset_potion.png") do (
  powershell -NoProfile -Command "[IO.File]::WriteAllBytes('%%F', [Convert]::FromBase64String((Get-Content ('%%F' + '.b64') -Raw)))"
  echo decode: %%F
)
echo Termine ! Double-cliquez maintenant sur dist\Potions-de-Taille.mcaddon pour installer l'addon.
pause
