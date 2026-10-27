# Tako — Design Plan

Living design doc. Every mechanic and idea lives here. Items marked
**OPEN** are gaps still being grilled; **SETTLED** items have been decided.

## 1. Core concept
- Pitch: You start as an octopus and evolve. You pick adaptations that
  shape your build, and you have to eat to survive. **SETTLED**
- Player fantasy: you play the octopus and grow it into something new. **SETTLED**
- "Everything is kind of crab": the world leans toward crabs
  (carcinization?). Meaning still **OPEN** (see Q6)
- Platform: web game first. **SETTLED**
- Feel: chaotic, clever and relaxed at the same time. **SETTLED**
- Scope: solo hobby project, no deadline. **SETTLED**
- Genre: top-down 2D roguelite survivor, like Vampire Survivors / Brotato.
  Each run is one life. **SETTLED**
- Session length: **OPEN**

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
- **What it is:** Kills earn progress. At each threshold you choose 1 of
  several random adaptations (VS/Brotato style). On top of that, you partly
  become what you eat.
- **Why:** this is where builds get chaotic and clever.
- **Rules & numbers:** number of choices per pick, rerolls, whether
  adaptations stack/upgrade, how eating changes you: **OPEN**
- **Status:** core SETTLED, details OPEN

### 3.2 Hunger
- **What it is:** a food meter that drains over time.
- **Rules:** hunger can't kill you. When the meter is empty you move slower
  and your attacks deal less damage. You don't shrink. **SETTLED**
- **Where food comes from / drain rate:** **OPEN**
- **Status:** core SETTLED, details OPEN

### 3.3 Death & runs
- **What it is:** when you die, the run restarts from scratch. Nothing
  carries over (no meta-progression). **SETTLED**
- **What kills you:** enemies (hunger can't). The health system is **OPEN**

## 4. Ideas backlog
_Unsorted ideas not yet promoted to mechanics._
- Crab world: everything tends toward crab. Meaning still being clarified.

## 5. Win / lose / scoring
- **OPEN**

## 6. Progression & economy
- **OPEN**

## 7. World, setting & tone
- **OPEN**

## 8. Scope & tech
- Engine / language: **OPEN**
- MVP feature cut: **OPEN**

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
