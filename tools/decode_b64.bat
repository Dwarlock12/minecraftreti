@echo off
cd /d "%~dp0.."
powershell -NoProfile -ExecutionPolicy Bypass -Command "$files = @('dist\Potions-de-Taille.mcaddon','dist\PotionsTaille_BP.mcpack','dist\PotionsTaille_RP.mcpack'); foreach ($f in $files) { $b64 = ((Get-ChildItem -Path ($f + '.b64.part*') | Sort-Object Name | ForEach-Object { (Get-Content $_ -Raw) -replace '\s','' }) -join ''); [IO.File]::WriteAllBytes($f, [Convert]::FromBase64String($b64)); Write-Host ('decode: ' + $f) }; Write-Host 'Termine ! Double-cliquez maintenant sur dist\Potions-de-Taille.mcaddon pour installer l addon. (Icones src/ : python tools\make_textures.py)'"
pause
