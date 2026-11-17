import { world, system } from "@minecraft/server";

const STEPS = [1.0, 0.8, 0.6, 0.4, 0.2];

function nextStep(current) {
  for (const step of STEPS) {
    if (current > step + 0.001) {
      return step;
    }
  }
  return 1.0;
}

function getScale(player) {
  const component = player.getComponent("minecraft:scale");
  if (component && component.valid) {
    return component.value;
  }
  return 1.0;
}

function applyScale(player, value) {
  const component = player.getComponent("minecraft:scale");
  if (!component || !component.valid) {
    throw new Error("composant minecraft:scale indisponible sur le joueur");
  }
  component.value = value;
  return component.value;
}

world.afterEvents.itemCompleteUse.subscribe((event) => {
  const player = event.source;
  const item = event.itemStack;
  if (!player || player.typeId !== "minecraft:player" || !item) {
    return;
  }

  const isReset = item.typeId === "mini:reset_potion";
  if (!isReset && item.typeId !== "mini:shrink_potion") {
    return;
  }

  const target = isReset ? 1.0 : nextStep(getScale(player));
  player.sendMessage(`§bTaille visée : §f${Math.round(target * 100)} %`);
  player.playSound("random.drink", { pitch: isReset ? 1.5 : 1.1, volume: 1.0 });

  system.run(() => {
    try {
      const applied = applyScale(player, target);
      player.sendMessage(`§aOK : échelle ${Math.round(applied * 100)} % §7(visible en vue 3e personne F5 ou par les autres joueurs)`);
    } catch (error) {
      player.sendMessage(`§cÉchec : ${error}`);
    }
  });
});
