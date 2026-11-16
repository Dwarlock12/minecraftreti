import { world } from "@minecraft/server";

const STEPS = [1.0, 0.8, 0.6, 0.4, 0.2];

function getScale(player) {
  const component = player.getComponent("minecraft:scale");
  if (component && component.valid) {
    return component.value;
  }
  return 1.0;
}

function setScale(player, value) {
  const component = player.getComponent("minecraft:scale");
  if (component && component.valid) {
    component.value = value;
  }
}

world.afterEvents.itemCompleteUse.subscribe((event) => {
  const player = event.source;
  const item = event.itemStack;
  if (!player || player.typeId !== "minecraft:player" || !item) {
    return;
  }

  if (item.typeId === "mini:shrink_potion") {
    const current = getScale(player);
    let next = 1.0;
    for (const step of STEPS) {
      if (current > step + 0.001) {
        next = step;
        break;
      }
    }
    setScale(player, next);
    player.sendMessage(`§bTaille actuelle : §f${Math.round(next * 100)} %`);
    player.playSound("random.drink", { pitch: 1.1, volume: 1.0 });
  } else if (item.typeId === "mini:reset_potion") {
    setScale(player, 1.0);
    player.sendMessage("§aTaille normale rétablie : §f100 %");
    player.playSound("random.drink", { pitch: 1.5, volume: 1.0 });
  }
});
