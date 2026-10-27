# Tako — Design Plan

Living design doc. Every mechanic and idea lives here. Items marked
**OPEN** are gaps still being grilled; **SETTLED** items have been decided.

## 1. Core concept
- Pitch: You start as an octopus and evolve. You pick adaptations that
  shape your build, and you have to eat to survive. **SETTLED**
- Player fantasy: you play the octopus and grow it into something new. **SETTLED**
- Style reference: **Everything is Crab** (animal-evolution roguelite,
  released 2026). It's a joke about carcinization: every creature
  eventually evolves into a crab. Tako should feel like that game. **SETTLED**
  - In that game you hunt creatures, eat them for XP, and pick 1 of 3
    mutations each level-up. Some mutations rule out others (antlers vs.
    horns). Attacks are manual, based on timing and dodging. Runs last about
    20 minutes with bosses.
- Platform: web game first. **SETTLED**
- Feel: chaotic, clever and relaxed at the same time. **SETTLED**
- Scope: solo hobby project, no deadline. **SETTLED**
- Genre: top-down 2D evolution roguelite. Each run is one life. **SETTLED**
- Run length: endless, no set end. **SETTLED**
- Controls: keyboard only for now. Keyboard + mouse and touch later. **SETTLED**

## 2. Core loop
- Moment-to-moment (seconds): **OPEN**
- Session loop (minutes): **OPEN**
- Long-term loop (progression across sessions): **OPEN**

## 3. Mechanics
_One subsection per mechanic. Template:_

### 3.x <Mechanic name>
- **What it is:**
- **Why it exists (what it adds to the loop):**
- **Inputs / controls:**
- **Rules & numbers:**
- **Interacts with:**
- **Failure / edge cases:**
- **Status:** OPEN

### 3.1 Adaptations (build)
- **What it is:** Eating what you kill gives XP. Fruit gives none (it only
  refills health and hunger). Each level-up you choose 1 of several random
  adaptations. On top of that, you partly become what you eat (see 3.7). **SETTLED**
- **Why:** this is where builds get chaotic and clever.
- **Body slots:** mutations go into body slots. Stacking works two ways:
  picking the same mutation again upgrades it, and a slot can hold more
  than one mutation. Each slot holds up to **2** mutations. **SETTLED**
- **Starting mutation list (first version):** **SETTLED**

  | # | Mutation | Slot | Key | What it does |
  |---|----------|------|-----|--------------|
  | 1 | Claw | Tentacles | L | Pinch attack, short range, hits hard |
  | 2 | Crab Shell | Back | – | Take less damage, move a bit slower (crab part) |
  | 3 | Crab Legs | Tentacles | – | Fast on land, slow in water (crab part) |
  | 4 | Fins | Back | – | Fast in water |
  | 5 | Big Mouth | Mouth | K | Bite attack that heals you a little |
  | 6 | Spikes | Skin | – | Hurts anything that touches you |
  | 7 | Horn | Head | Space | Charge forward |
  | 8 | Extra Eyes | Head | – | See farther (camera zooms out) |
  | 9 | Stretchy Tentacle | Tentacles | J upgrade | The slap reaches farther |
  | 10 | Stomach | Mouth | – | Hunger drains slower |
- **Picks:** choose 1 of 3, with a few rerolls per run. **SETTLED**
- **Rules & numbers:** number of choices per pick, rerolls, whether
  adaptations stack/upgrade, how eating changes you: **OPEN**
- **Status:** core SETTLED, details OPEN

### 3.1b Creature behavior
- Prey runs away (fish, small crabs), predators hunt you (sharks,
  seagulls), and neutral creatures only fight back when you hit them. **SETTLED**
- First-version creatures (beach): **Small Crab** (prey, runs away),
  **Seagull** (predator, dives at you), **Hermit Crab** (neutral, fights
  back when hit). **SETTLED**
- **Duck:** the rarest creature, and super funny. Details are **OPEN**

### 3.2 Hunger
- **What it is:** a food meter that drains over time.
- **Rules:** hunger can't kill you. When the meter is empty you move slower
  and your attacks deal less damage. You don't shrink. **SETTLED**
- **Drain rate:** slow and relaxed. An empty meter only makes you slower
  and weaker. **SETTLED**
- **Status:** core SETTLED, details OPEN

### 3.3 Death & runs
- **What it is:** when you die, the run restarts from scratch. Nothing
  carries over (no meta-progression). **SETTLED**
- **What kills you:** enemies (hunger can't).

### 3.4 Health
- A health bar that eating refills. **SETTLED**

### 3.5 Food sources
- Killed animals (eat what's left after the kill) and fruit from trees. **SETTLED**
- How much each heals or fills hunger: **OPEN**

### 3.6 Combat / abilities
- Abilities fire when you press a button (not automatic). **SETTLED**
- Keys: WASD to move. J / K / L / Space are 4 ability slots. Abilities fire
  the way you're facing. **SETTLED**
- Mutations that give an attack fill these slots. Mouse aiming comes later. **SETTLED**
- Starting kit: tentacle slap only. No ink cloud. **SETTLED**
- Keys tied to body parts: some slots come with an attack, and each one has a
  fixed key. Suggested: J = tentacles, K = mouth, L = claws, Space =
  special. **SETTLED** (exact mapping can still change)

### 3.8 Zones
- Ocean (fish, squid), beach (crabs) and inland (fruit trees, land
  animals). Each zone has different food and enemies. **SETTLED**
- Some parts work better in one zone (fins are fast in water, legs are fast
  on land). **SETTLED**

### 3.9 Bosses
- A giant creature (King Crab, Giant Seagull, ...) appears about every
  5 minutes. Killing it gives a guaranteed rare mutation. **SETTLED**

### 3.7 Become what you eat
- Eating a creature type makes its adaptations show up more often in your
  picks. **SETTLED**

## 4. Ideas backlog
_Unsorted ideas not yet promoted to mechanics._
- Crab pull: the longer you survive, the more crab parts show up in your
  picks. Going full crab does nothing special; it's just funny. **SETTLED**

## 5. Win / lose / scoring
- No score. The fun is seeing what you turn into. A run ends when you die. **SETTLED**
- When you die: a creature card showing your parts and how long you
  survived. **SETTLED**
- Difficulty: rises over time, with bosses now and then. **SETTLED**

## 6. Progression & economy
- **OPEN**

## 7. World, setting & tone
- Tone: silly, not super realistic. **SETTLED**
- Setting: beach, ocean and land. You can crawl out of the water. **SETTLED**
- Map: infinite, randomly generated islands in an endless ocean, each
  island ringed by beach. **SETTLED**
- Art: the designer hand-draws it. Claude helps turn the drawings into game
  sprites, possibly pixelized. The code uses simple shapes until the art is
  ready. Pixel vs. cartoon: **OPEN**
- Sound: none in the first version. **SETTLED**

## 8. Scope & tech
- Engine: **Phaser** (JavaScript, web). **SETTLED** (Everything is Crab uses
  Unity, but Phaser was chosen for the web.)
- Who builds it: another Claude Code session will write the code from
  this plan. The designer doesn't code. **SETTLED**
- First playable version: **SETTLED**
  - Octopus with a tentacle slap (J)
  - One zone (the beach)
  - 3 enemy types (prey, predator, neutral)
  - Fruit, health bar, hunger meter
  - Eating gives XP; choose 1 of 3 at each level-up
  - About 10 mutations
  - Creature card when you die
  - Later: bosses, other zones, rerolls, mouse/touch, sound
- Hosting: GitHub Pages (itch.io later). **SETTLED**

## 9. Decision log
| # | Decision | Answer | Date |
|---|----------|--------|------|
| 1 | Player character | An octopus that evolves through adaptations | 2026-10-27 |
| 2 | Platform | Web game first | 2026-10-27 |
| 3 | Experience goal | Chaotic, clever and relaxed | 2026-10-27 |
| 4 | Scope | Solo hobby project | 2026-10-27 |
| 5 | Genre | Top-down 2D roguelite survivor | 2026-10-27 |
| 6 | Adaptation source | Kills earn picks (choose from random options), plus partly becoming what you eat | 2026-10-27 |
| 7 | Hunger | Empty meter means slower and weaker; no shrinking, no death | 2026-10-27 |
| 8 | Death | Full restart, no meta-progression | 2026-10-27 |
| 9 | Style reference | Everything is Crab | 2026-10-27 |
| 10 | Attacks | Press-a-button abilities | 2026-10-27 |
| 11 | Food | Animal kills and tree fruit | 2026-10-27 |
| 12 | Run length | Endless | 2026-10-27 |
| 13 | Health | Health bar, healed by eating | 2026-10-27 |
| 14 | Become what you eat | Eating a creature biases your picks toward its adaptations | 2026-10-27 |
| 15 | Controls | Keyboard only for now | 2026-10-27 |
| 16 | XP source | Eating kills gives XP; fruit gives none | 2026-10-27 |
| 17 | Ability keys | WASD to move, J/K/L/Space for abilities, aimed where you're facing | 2026-10-27 |
| 18 | Scoring | No score | 2026-10-27 |
| 19 | Tone | Silly, not realistic | 2026-10-27 |
| 20 | Body slots | Slots, and stacking is also allowed | 2026-10-27 |
| 21 | Difficulty | Rises over time, plus bosses | 2026-10-27 |
| 22 | Crab pull | Crab parts show up more the longer you survive | 2026-10-27 |
| 23 | Starting kit | Tentacle slap only | 2026-10-27 |
| 24 | Setting | Beach, ocean, land | 2026-10-27 |
| 25 | Death screen | Creature card | 2026-10-27 |
| 26 | Hunger drain | Slow | 2026-10-27 |
| 27 | Stacking | Repeat picks upgrade, and a slot can hold several | 2026-10-27 |
| 28 | Keys vs. slots | Each attack slot has a fixed key | 2026-10-27 |
| 29 | Picks | 1 of 3, with a few rerolls | 2026-10-27 |
| 30 | Zones | Different food/enemies per zone, and some parts suit a zone | 2026-10-27 |
| 31 | Bosses | About every 5 minutes, drop a rare mutation | 2026-10-27 |
| 32 | Full crab | Nothing special, just funny | 2026-10-27 |
| 33 | Engine | Phaser | 2026-10-27 |
| 34 | Builder | Another Claude session codes it | 2026-10-27 |
| 35 | Creature behavior | Prey, predators, neutral | 2026-10-27 |
| 36 | Map | Infinite, randomly generated | 2026-10-27 |
| 37 | Art | Cartoon; shapes for prototyping | 2026-10-27 |
| 38 | First version | Scope as listed in section 8 | 2026-10-27 |
| 39 | Mutations per slot | 2 | 2026-10-27 |
| 40 | Zone layout | Islands in an endless ocean | 2026-10-27 |
| 41 | Art source | Designer draws; Claude helps pixelize | 2026-10-27 |
| 42 | Mutations | Starter list of 10 accepted | 2026-10-27 |
| 43 | Creatures | Small Crab, Seagull, Hermit Crab, plus a rare Duck | 2026-10-27 |
| 44 | Hosting | GitHub Pages | 2026-10-27 |
| 45 | Sound | None in the first version | 2026-10-27 |
