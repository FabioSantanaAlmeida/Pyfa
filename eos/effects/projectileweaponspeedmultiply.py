# projectileWeaponSpeedMultiply
#
# Used by:
# Modules from group: Gyrostabilizer (14 of 14)
type = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Projectile Weapon",
                                     "speed", module.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties=True)
