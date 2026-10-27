# Tako — Design Plan

Living design doc for Tako. Every mechanic and idea lives here, and a
coding session builds from it. Items marked **OPEN** would be gaps still being
decided. Everything else has been settled with the designer. The decision
log at the bottom records each answer.

## 1. Core concept
- **Pitch:** You start as an octopus and evolve. You eat what you kill, pick
  mutations that shape your body and your build, and see what silly creature
  you turn into before you die.
- **Style reference:** *Everything is Crab* (Odd Dreams Digital, 2026), an
  animal-evolution roguelite built on the carcinization joke: every creature
  eventually evolves into a crab. Tako should feel like that game. In it you
  hunt creatures, eat them for XP, pick 1 of 3 mutations each level-up, and
  fight by timing and dodging (no auto-attacks).
- **Feel:** chaotic, clever and relaxed at the same time.
- **Tone:** silly, not realistic.
- **Platform:** web game (browser).
- **Genre:** top-down 2D evolution roguelite. Each run is one life.
- **Scope:** solo hobby project, no deadline. The designer designs and
  draws. A Claude Code session writes the code.

## 2. Core loop
- **Moment to moment (seconds):** swim and crawl around with WASD, hit
  creatures with your ability keys, dodge predators, and eat what's left
  after a kill (or fruit).
- **Run (minutes):** eating kills → XP → level up → choose 1 of 3 mutations
  → your body and attacks change → take on tougher creatures. Difficulty
  rises over time, and a boss shows up about every 5 minutes. Runs are
  endless and only end when you die.
- **After a run:** a creature card shows what you became. You start over from
  scratch. Nothing that affects gameplay carries over.
- **Across runs (version 2):** a house that collects your past creatures,
  the animals you've eaten, and cosmetics you unlock. For show only.

## 3. Mechanics

### 3.1 Eating, XP & level-ups
- Killed animals leave food. Eating it gives **XP**, health and hunger.
- **Fruit** from trees gives health and hunger but **no XP**.
- Each level-up: choose **1 of 3** random mutations.
- **Rerolls:** a few per run (not in the first version).
- **Become what you eat:** eating a creature type makes its mutations show
  up more often in your picks.
- **Crab pull:** the longer you survive, the more crab parts show up in
  your picks. Going full crab does nothing special; it's just funny.

### 3.2 Body slots & mutations
- Body slots: **head, mouth, tentacles, back, skin**.
- Each slot holds up to **2** mutations. Picking a mutation you already have
  **upgrades** it instead.
- Every mutation shows up on the octopus's body as its own drawn piece.
- **Starting list (first version):**

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
  | 9 | Stretchy Tentacle | Tentacles | J (upgrade) | The slap reaches farther |
  | 10 | Stomach | Mouth | – | Hunger drains slower |
  | 11 | Duck Bill | Mouth | K | Only from eating the Duck. Your bite quacks and stuns |

### 3.3 Combat & controls
- Keyboard only for now. Mouse aiming and touch come later.
- **WASD** to move. **J / K / L / Space** are the 4 ability keys.
- Abilities fire when you press their key (no auto-attacks), in the
  direction you're facing.
- Starting kit: **tentacle slap (J)** only.
- Keys go by attack type, not body slot: J = tentacle attacks, K = mouth
  attacks, L = claw attacks, Space = special (charge, etc.).
- When two attacks share a key (for example, Big Mouth + Duck Bill on K),
  pressing it fires **both at once**. You never lose an attack you picked.

### 3.4 Health & hunger
- **Health bar**, refilled by eating. Enemies are the only thing that can
  kill you.
- **Hunger meter** drains slowly. Hunger can't kill you. When it's empty you
  move slower and your attacks deal less damage. You don't shrink.

### 3.5 Creatures
- **Prey** run away, **predators** hunt you, and **neutral** creatures only
  fight back when you hit them.
- First-version creatures (beach):
  - **Small Crab:** prey, runs away.
  - **Seagull:** predator, dives at you.
  - **Hermit Crab:** neutral, fights back when hit.
  - **Duck:** the rarest creature, about once every 3 runs. It waddles
    around looking harmless, but it's secretly the strongest thing in the
    game. Eating it always gives Duck Bill.
- Later zones: ocean (fish, squid, sharks) and inland (land animals).

### 3.6 Bosses (later)
- A giant creature (King Crab, Giant Seagull, ...) appears about every
  5 minutes. Killing it gives a guaranteed rare mutation.

### 3.7 Death & the creature card
- When you die, a creature card shows your body, your mutations and how long
  you survived. Then you start a new run from scratch.
- No score.

## 4. World
- **Map:** infinite and randomly generated. Islands in an endless ocean,
  each ringed by beach.
- **Zones:** ocean, beach and inland, each with its own food and creatures.
  Some parts work better in a zone (fins are fast in water, legs are fast on
  land).
- Difficulty rises over **time**, not distance.

## 5. Home / house (version 2)
- For show only: no power boosts.
- **Collection book:** a page for every creature you've eaten.
- **Living house:** the animals you've eaten and the creatures you made in
  past runs walk around in it.
- **Wall of creature cards:** each run's death card hangs like a picture
  frame.
- **Customization:** octopus color/pattern, plus hats and accessories,
  unlocked by milestones (eat 10 ducks → duck hat, survive 15 minutes →
  crown, ...).

## 6. Saving & accounts
- **First version:** saves run history (creature cards and animals eaten) in
  the browser on that device, so nothing is lost before the house exists.
- **Version 2:** cloud saves through **Supabase**. You can play without
  logging in (saved on the device) and sign in with **Google** later to move
  your saves to the cloud. The designer creates the free Supabase project.
- GitHub Pages only hosts the game files; Supabase stores the saves.

## 7. Art & sound
- **Style:** cartoon designs drawn as **pixel art** (no smooth lines).
- **Pipeline:** the designer draws on paper and uploads photos/scans to
  `art/raw/`. Claude converts them to pixel sprites. Each body part is a
  separate drawing so it can attach to the octopus.
- The code uses simple placeholder shapes until the art is ready.
- **Sound:** none in the first version.

## 8. Tech & scope
- **Engine:** Phaser (JavaScript, web).
- **Hosting:** GitHub Pages (itch.io later).
- **Tuning:** the coding session chooses starting numbers (health, damage,
  speed, XP curve, spawn rates, rerolls) and keeps them all in **one
  settings file** for tuning through playtesting.
- **First playable version:**
  - Octopus with a tentacle slap (J), WASD movement
  - Beach zone only, on randomly generated islands
  - Small Crab, Seagull, Hermit Crab and the rare Duck
  - Fruit trees, health bar, hunger meter
  - Eating gives XP; choose 1 of 3 at each level-up
  - The 11 mutations above, with body slots (2 per slot)
  - Crab pull and become-what-you-eat weighting on picks
  - Creature card when you die, with run history saved on the device
  - Placeholder shapes for art
- **Later:** ocean and inland zones, bosses, rerolls, sound, mouse/touch,
  house + customization + cloud saves (version 2), itch.io.

## 9. Ideas backlog
_New ideas go here before they become mechanics._
- (empty — add new ideas here)

## 10. Decision log
| # | Decision | Answer |
|---|----------|--------|
| 1 | Player character | An octopus that evolves through mutations |
| 2 | Platform | Web game |
| 3 | Experience goal | Chaotic, clever and relaxed |
| 4 | Scope | Solo hobby project |
| 5 | Genre | Top-down 2D evolution roguelite |
| 6 | Style reference | Everything is Crab |
| 7 | XP source | Eating kills gives XP; fruit gives none |
| 8 | Picks | 1 of 3, with a few rerolls (rerolls later) |
| 9 | Become what you eat | Eating a creature biases picks toward its mutations |
| 10 | Crab pull | Crab parts show up more the longer you survive; full crab is just funny |
| 11 | Body slots | Slots, 2 mutations each; repeat picks upgrade |
| 12 | Attacks | Press-a-button, aimed where you're facing |
| 13 | Controls | WASD + J/K/L/Space, keyboard only for now |
| 14 | Starting kit | Tentacle slap only, no ink |
| 15 | Health | Health bar, healed by eating |
| 16 | Hunger | Drains slowly; empty means slower and weaker, never death |
| 17 | Food | Animal kills and tree fruit |
| 18 | Creature behavior | Prey, predators, neutral |
| 19 | First creatures | Small Crab, Seagull, Hermit Crab, rare Duck |
| 20 | Duck | Secretly deadly, gives Duck Bill, about 1 in 3 runs |
| 21 | Bosses | About every 5 minutes, drop a rare mutation |
| 22 | Run length | Endless; difficulty rises over time |
| 23 | Death | Creature card, full restart, no score |
| 24 | Setting | Beach, ocean, land |
| 25 | Map | Infinite random islands in an endless ocean |
| 26 | Zones | Different food/enemies per zone; some parts suit a zone |
| 27 | Tone | Silly, not realistic |
| 28 | Art | Cartoon designs drawn as pixel art, from paper drawings |
| 29 | Sound | None in the first version |
| 30 | Engine | Phaser |
| 31 | Hosting | GitHub Pages |
| 32 | Builder | A Claude Code session writes the code |
| 33 | Numbers | One settings file, tuned through playtesting |
| 34 | House | Version 2, for show only |
| 35 | House contents | Collection book, walking animals and past creatures, card wall |
| 36 | Customization | Color/pattern + hats/accessories, unlocked by milestones |
| 37 | Saving | Device first; Supabase cloud saves in version 2 |
| 38 | Login | Play without logging in; Google sign-in later |
| 39 | First-version saving | Run history saved on the device |
| 40 | Shared keys | Keys go by attack type; attacks on the same key fire together |
| 41 | Duck in first version | Yes, with Duck Bill |
