# ===========================================
# CREATE GAME GUIDES FILE
# ===========================================

file_content = """
====================================================================
                       WILD WEST ZOMBIE SURVIVAL
====================================================================

HELP
The Wild West is overrun by zombies: Runners, Normals, Bombers, Tankers,
Igniters, and Outlaws. Survive, craft weapons, set traps, and fight 
to endure up to 999 nights.

Tutorial:
- Shoot zombies and set traps to survive.
- Jump, crouch, and sprint to avoid damage (stamina 100).
- Collect materials and coins for crafting or buying ammo/guns.
- Watch zombie types carefully:
    * Runner: fast, low HP, high damage
    * Normal: standard zombie
    * Bomber: explodes on contact
    * Tanker: high HP, huge damage, knockback
    * Igniter: throws fire bottles; fire burns over time
    * Outlaw: shoots until ammo is empty; can charge and infect

INFO
Achievements:
- FIRST_KILL      : Kill your first zombie
- NIGHT_OWL       : Survive 100 nights
- TAKE_A_SHOWER   : Survive 999 nights
- TRAPMASTER      : Kill zombies using traps
- MUSKET_MASTER   : Craft and use a musket

Game Mechanics:
- Player HP: 100
- Stamina: 100
- Ammo: found in chests or houses
- Guns: Revolver, Rifle, Shotgun, Musket (unlock at night 150)
- Materials: used for crafting traps or special weapons
- Stores: buy ammo, guns, materials (closed at night)
- Traps: kill zombies when set properly

ANTI-CHEAT SYSTEM
- First offense: warning
- Second offense: kick
- Third offense: ban

EXTENDED STORY
The year is 1887. The once lawless but peaceful towns of the Wild West
have fallen into chaos. A mysterious plague rises from the graves,
bringing forth the undead in terrifying forms: swift Runners,
explosive Bombers, relentless Tankers, fire-wielding Igniters, and
deadly Outlaws who shoot and infect their victims. Survive up to 999
nights, face increasingly dangerous hordes, and uncover the secrets
behind the plague. Prepare yourself. The Wild West is no longer yours.
====================================================================
"""

# Create and write to file
file_name = "WILD_WEST_ZOMBIE_SURVIVAL_GUIDES.txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write(file_content)

print(f"File '{file_name}' has been created successfully!")
