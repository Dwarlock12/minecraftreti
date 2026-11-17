# Potions de Taille — Addon Minecraft Bedrock (Windows 10)

Addon prêt à installer : deux potions buvables qui changent la taille de votre
personnage.

- **Potion de rétrécissement** (fiole bleue, flèche vers le bas) : chaque gorgée
  descend d'un palier — 100 % → 80 % → 60 % → 40 % → 20 % — puis revient à 100 %.
- **Potion de taille normale** (fiole verte, flèche vers le haut) : retour direct
  à 100 %.

Un message dans le chat et un son confirment chaque changement.

## Installation (Windows 10)

### Depuis ce dépôt GitHub (recommandé, aucun programme à installer)

1. Téléchargez le dépôt : bouton **Code → Download ZIP**, puis décompressez le ZIP.
2. Double-cliquez sur `tools\build.bat` (Windows 10 : PowerShell est inclus,
   aucun programme à installer). Il génère `dist\Potions-de-Taille.mcaddon`
   et les deux `.mcpack` à partir des sources texte (les 2 icônes PNG 16×16
   sont embarquées dans `tools\build.ps1`).
3. Double-cliquez sur `dist\Potions-de-Taille.mcaddon`.
   Minecraft s'ouvre et affiche une notification « import réussi ».
4. Ouvrez (ou créez) un monde, puis allez dans **Paramètres** (engrenage) :
   - **Packs de comportement** → activez **« Potions de Taille »**
     (le pack de ressources se coche automatiquement grâce à la dépendance).
   - Sinon, activez aussi **« Potions de Taille - Ressources »** dans
     **Packs de ressources**.
5. C'est prêt. Les potions sont dans l'inventaire créatif (onglet Objets) ou
   obtenables avec la commande (trichets activés) :

   ```
   /give @s mini:shrink_potion
   /give @s mini:reset_potion
   ```

## Utilisation

Clic droit **maintenu** environ 1,6 seconde pour boire la potion.

## ⚠️ Bon à savoir (comportement Bedrock)

- Le changement de taille est **visuel** (composant `minecraft:scale` = taille du modèle).
- En **vue première personne**, on ne voit pas son propre corps : passez en
  **vue troisième personne (touche F5)** ou faites-vous observer par un autre
  joueur pour voir la différence.
- La **hitbox / collision ne change pas** (limitation Bedrock documentée).
- Un message confirme la valeur réellement appliquée après écriture du composant.

## Désinstallation

Dans le monde : Paramètres → packs → désactivez « Potions de Taille ».
Ou supprimez les dossiers correspondants dans :

```
%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\behavior_packs
%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\resource_packs
```

## Technique

- API stable `@minecraft/server` **1.17.0** (le composant `minecraft:scale`
  y est modifiable ; aucune option expérimentale requise).
- Fonctionne sur Minecraft Bedrock ≥ 1.21.0 (Windows 10 inclus).
- Le redimensionnement est appliqué via le composant `minecraft:scale` du
  joueur à la consommation de l'objet (événement `itemCompleteUse`) :
  c'est un effet visuel sur le modèle du joueur.
- Structure : `PotionsTaille_BP` (comportement : items + script) et
  `PotionsTaille_RP` (ressources : icônes PNG 16×16 + textes fr/en),
  embarqués dans `Potions-de-Taille.mcaddon`.

## Reconstruire les archives

```bash
python3 tools/make_textures.py   # régénère les icônes PNG
python3 tools/build.py           # régénère dist/*.mcpack et dist/*.mcaddon
```

Sans Python : `tools\build.bat` (Windows, PowerShell) génère les archives directement.

## Pourquoi un `build.bat` (dépôt 100 % texte) ?

Les archives (`.mcaddon`, `.mcpack`) et les icônes (`.png`) sont binaires ; pour
garantir qu'aucun octet n'est altéré, le dépôt ne contient que du texte :
sources des packs + `tools/build.ps1`, qui embarque les 2 icônes 16×16 en base64
et reconstruit les archives avec `ZipFile` (.NET intégré à Windows 10).
Les anciens fichiers `.b64.partNN` sont obsolètes (fichiers neutralisés).
Rebuild manuel : `python3 tools/make_textures.py && python3 tools/build.py`.
