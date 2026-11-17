$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$base = Split-Path -Parent $root
$src = Join-Path $base 'src'
$dist = Join-Path $base 'dist'
$bpDir = Join-Path $src 'PotionsTaille_BP'
$rpDir = Join-Path $src 'PotionsTaille_RP'
$rpItems = Join-Path $rpDir 'textures' 'items'
$bpPack = Join-Path $dist 'PotionsTaille_BP.mcpack'
$rpPack = Join-Path $dist 'PotionsTaille_RP.mcpack'
$addon = Join-Path $dist 'Potions-de-Taille.mcaddon'

$shrinkPngB64 = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAWUlEQVR42mNgoBXQ1tb+j4zJMuDYk//7QHgIGgDzN7IBRBuCrBEdEzQEn2aiDAFJAsEzigwAKVIp+f8fFyZoAD7NJBvA47APjEk2AKYRHdPPBRSFATEYWQ8AJlodDXwEiWQAAAAASUVORK5CYII='
$resetPngB64 = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAWUlEQVR42mNgoBXQ1tb+j4zJMuDYk//7QHgIGgDzN7IBRBuCrBEdEzQEn2aiDAFJAsEzigwAKTI5G/AfFyZoALJisR5dMCbZAJhGdEw/F1AtDMgygBiMrAcAe4MQoTP/jKUAAAAASUVORK5CYII='
[IO.File]::WriteAllBytes((Join-Path $rpItems 'shrink_potion.png'), [Convert]::FromBase64String($shrinkPngB64))
[IO.File]::WriteAllBytes((Join-Path $rpItems 'reset_potion.png'), [Convert]::FromBase64String($resetPngB64))
Write-Host 'Icones PNG decodees (16x16).'

Add-Type -AssemblyName System.IO.Compression.FileSystem

function Copy-ToEntry($entry, $file) {
  $inStream = [IO.File]::OpenRead($file)
  try {
    $outStream = $entry.Open()
    try { $inStream.CopyTo($outStream) } finally { $outStream.Dispose() }
  } finally { $inStream.Dispose() }
}

function New-Pack($srcDir, $outPath) {
  if (Test-Path $outPath) { Remove-Item $outPath -Force }
  $srcFull = [IO.Path]::GetFullPath($srcDir)
  $zip = [System.IO.Compression.ZipFile]::Open($outPath, 'Create')
  try {
    Get-ChildItem -Path $srcFull -Recurse -File |
      Where-Object { $_.Name -notlike '*.b64*' } |
      Sort-Object FullName |
      ForEach-Object {
        $rel = $_.FullName.Substring($srcFull.Length + 1) -replace '\\', '/'
        $entry = $zip.CreateEntry($rel)
        $entry.LastWriteTime = [DateTimeOffset]::new(1980, 1, 1, 0, 0, 0, [TimeSpan]::Zero)
        Copy-ToEntry $entry $_.FullName
        Write-Host ('  + ' + $rel)
      }
  } finally { $zip.Dispose() }
  Write-Host ('Pack cree: ' + $outPath)
}

New-Pack $bpDir $bpPack
New-Pack $rpDir $rpPack

if (Test-Path $addon) { Remove-Item $addon -Force }
$zip = [System.IO.Compression.ZipFile]::Open($addon, 'Create')
try {
  foreach ($p in @($bpPack, $rpPack)) {
    $entry = $zip.CreateEntry([IO.Path]::GetFileName($p))
    $entry.LastWriteTime = [DateTimeOffset]::new(1980, 1, 1, 0, 0, 0, [TimeSpan]::Zero)
    Copy-ToEntry $entry $p
  }
} finally { $zip.Dispose() }

Write-Host ('OK: ' + $addon)
Write-Host 'Double-cliquez maintenant sur dist\Potions-de-Taille.mcaddon pour installer l addon.'
