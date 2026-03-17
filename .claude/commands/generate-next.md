First, ask me: **"Which day are you training? (A, B, or C)"** — wait for my answer before continuing.

Once I answer, load the corresponding routine from the `routines/` folder:
- Day A → `routines/day-A.md`
- Day B → `routines/day-B.md`
- Day C → `routines/day-C.md`

The routine file defines the exercises, target rep ranges, and muscle focus for that day. Use it as the blueprint — these are the exercises to program, in order.

Then fetch two things using MCP:
1. **My last workout for that day** (search recent workouts for the matching day) — to get actual sets, reps, RPE, weights performed, and any notes I left on exercises. **Exercise notes take high priority** — if I noted why I used a lighter weight, flagged something to change, or said what I want next time, honour that directly in the next session.
2. **The most recent Hevy routine for that day** (use `get-routines`, find the most recent "Day X" routine by date in the name) — to see what was planned for that session.

**Before proposing the next session**, output a performance summary block. Start with a header like:

```
I have the last Day B workout ("Day B - 4/3", March 9) and the matching routine. Here's the breakdown:

---
Performance Summary — Last Day B (9 March)
```

**Missing or extra sets:** If the logged workout has fewer sets than the routine prescribed for an exercise (or more), and there's no note explaining why, **ask me before continuing** — e.g. "Hammer Curl shows 2 logged sets but the routine had 3 — did you skip a set or forget to log it?" Base the next session on my answer, not on assumptions.

Then for each exercise, compare the last workout against the routine that was active for it. Note whether targets were hit, exceeded, or missed — and if I left a note on an exercise, include it and explain how it influenced the next session. Use this to give honest, specific feedback — e.g. "You hit all your bench targets", "You fell 2 reps short on lat pulldowns on the last set — consider staying at this weight", "You noted the dumbbells felt too light — going up next session". End with an overall verdict on how the session went.

Then propose the next session, and only after that ask: **"Happy with this, or want any changes?"**

## Weight selection

**All weights are in kg — never use lbs.** Before setting any weight, read `weights.md` — it lists the exact available weights for each equipment type (cable, lat pulldown, barbell, etc.). Only use values from that file. If the ideal progression weight isn't available, pick the closest option:
- If the next weight up is available, use it.
- If not, use the nearest **lower** weight and compensate with more reps or an extra set.
- Alternatively, use the nearest **higher** weight with fewer reps or sets — whichever makes more sense given the exercise and progression context.

Follow these progression rules:

1. **Progressive overload priority:** Increase volume (sets/reps) first. Only increase weight once I've hit the top of the rep range across all sets.
2. **Don't stall me:** If I missed a target by just 1 rep on one set but hit everything else, still progress me — don't hold me back for a minor miss.
3. **Half reps as finishers:** For isolation exercises (e.g., curls, lateral raises, flyes), add a set of half reps at the end to maximize time under tension. Don't add half reps to heavy compound lifts.
4. **Cap weight jumps at 25% of current load:** When increasing weight, the increment must not exceed 25% of the current working weight. If the next available dumbbell/plate increment would exceed this (e.g. 2.5kg → 5kg is a 100% jump), do NOT increase weight — keep the same weight and note the rep ceiling was hit, or add a set instead.

---

## Warm-up protocol

The routine file may include a **Warm-up Sets** column. When it does:
- The percentages are of the working weight for that exercise.
- Warm-up sets are NOT to failure — brisk and controlled, saving energy for working sets.
- Rest ~90 sec after the last warm-up before the first working set.
- Include the warm-up sets in the output under each relevant exercise so I know to do them.
- Exercises with `—` in the warm-up column need no warm-up (muscle is already primed from earlier in the session).

## Rest periods

The routine file may include a **Rest Between Sets** column. When it does:
- Include the prescribed rest duration in the output for each exercise.
- Compounds (bench, squat, deadlift, rows, pulldowns) typically require 2.5–3.5 min — this is intentional, especially in a caloric deficit.
- Isolation exercises (curls, lateral raises, extensions, abs) use 45–90 sec.
- Don't shorten rest periods to save time — inadequate rest causes performance to crater across sets and undermines progressive overload.

## Partial reps

The routine file may include a **Partial Reps?** column. General rules that apply across all days:
- **Only on the last set** of an isolation exercise — never on compounds, never on sets 1 or 2.
- **Only after hitting the minimum target reps** in full ROM. If the minimum wasn't reached, stop the set — don't extend with partials.
- **3–5 half reps maximum** — go straight from full reps to partials with no rest-pause.
- Where the column specifies a position (e.g. "bottom-half", "stretched position"), use that; it determines where in the ROM the partial is performed.
- Exercises marked "No" in the partial reps column should always be full ROM — no exceptions.
- **Full ROM always trumps partials for progression purposes.** If the routine prescribed half reps but I did full-ROM reps instead and hit the rep range, that's equal or better — progress me normally based on the full-ROM performance. Never hold me at the same weight/reps just because I skipped partials. Partials are a bonus, not a gate.

## Cycling (every session)

Every routine ends with a cycling block — always two sets, fixed targets:
- Set 1: 2.6 km in 16 minutes
- Set 2: 2.5 km in 15 minutes

Include this in the proposed workout output and in the Hevy routine when creating it. To get the `exerciseTemplateId` for cycling, search `get-exercise-templates` if it wasn't in the last workout. Notes for cycling: `"Set 1: 2.6km / 16min; Set 2: 2.5km / 15min"`.

---

## Should this routine be regenerated?

After fetching the last workout and the current routine for this day type, **compare them before doing any work** to see if the routine already reflects the last workout's performance.

### How to score similarity

Compare the current routine against the last workout, exercise by exercise (ignoring warm-up sets and cycling). For each exercise present in both, check whether the **working weight** matches (within 2.5kg). Count how many exercises match:

- **3+ exercises match on weight** → the routine is likely already up to date.
- **2 exercises match** → borderline — flag it but lean toward asking.
- **0–1 exercises match** → the routine is stale, proceed without asking.

Things that do **not** count as differences:
- Missing or extra warm-up sets
- A skipped final set or half-rep set
- 1–2 exercises missing entirely (the user may have skipped them)
- Minor rep count differences (e.g. routine says 10, workout logged 8)

Things that **do** count as differences:
- Working weights differ by more than 2.5kg on multiple exercises
- Exercises in the routine that weren't in the workout at all **and** have different weights from any prior session
- Completely different exercise selection (different movements, not just missing ones)

### What to do

If the score indicates the routine is already up to date (3+ weight matches), **ask before continuing**:
> "The current Day X routine already looks updated — X out of Y exercises match the weights from your last workout. Do you still want me to generate a new one?"

Only proceed if the user confirms. If the routine is clearly stale (0–1 matches), skip this check and proceed normally.

## Routine date — how to pick the right date for the new routine title

The routine title must reflect the date the session will actually take place, **not** the date you're generating it. Always calculate it fresh:

- Workout days are **Monday, Wednesday, Friday** only.
- Day types alternate: A → B → A → B → …
- Look at today's date and the last workout (which you already fetched). The last workout title tells you what day type was last done and when.
- The **next occurrence** of this day type is the first workout weekday (Mon/Wed/Fri) where this day type falls in the alternating sequence, starting from the day after the last workout.

**Example:** Today is Wednesday and the user just did Day A. The alternation from here is:
- Friday → Day B
- Monday → Day A ← next time Day A comes up
- Wednesday → Day B

So the new Day A routine should be titled `Day A - DD/MM` using **next Monday's date**.

**Example:** Today is Friday and the user just did Day B. The alternation:
- Monday → Day A
- Wednesday → Day B ← next time Day B comes up

So the new Day B routine should be titled `Day B - DD/MM` using **next Wednesday's date**.

**Title format:** `Day X - DD/MM` (no year, no weekday name). E.g. `Day A - 23/3`, `Day B - 25/3`.

---

Output format:
- Exercise name
- Sets × Reps (with weight)
- Any changes from last session, noted with the reason (e.g., "+1 set — hit all reps last time" or "+2.5kg — topped out rep range")

Example output:
```
Here's your next Day A session, based on today's workout:
  ---             
  Bench Press (Barbell)
  Nex time you do: 4 × 6–8 @ 27.5kg
  Expectation: +2.5kg — hit 4×8 (top of range) across all sets
  Before you did: 4x8 @ 25kg
  
  ---
  Lat Pulldown (Cable)
  ...
```

Note: The second lines for each exercise are a faded colour in the console.

After outputting the workout, ask: **"Happy with this, or want any changes?"**

- If they want changes, apply them and ask again.
- Once they're happy, ask: **"Should I create a new routine in Hevy?"**
- If yes, fetch the existing routine using `get-routines` to find the matching Day X routine. First, **rename the old routine** by calling `update-routine` to append "-OLD" to its title (e.g. "Day B - 4/3" becomes "Day B - 4/3-OLD"). Then call `create-routine` with the new exercises and sets. **Use the date calculated in the "Routine date" section above** — always the next upcoming workout weekday for this day type, never today's date and never reusing the old routine's date. Use the `exerciseTemplateId` values already seen in the last workout data — no need to look them up again. Set `reps` and `repRange: {start: reps, end: reps}` to the target rep count. Set `weightKg` to the target weight. For half-rep finisher sets, add them as additional sets with `reps` set to the target half-rep count.

  **Always populate the notes field for every exercise** — never leave it blank. The note should be a compact summary useful at-a-glance during the session. Include: sets × rep range, any half-rep instructions, and a short cue about progression or intent. Examples:
  - `"3 × 8–10; last set + 3 half reps (bottom); progressed from 25kg"`
  - `"4 × 6–8; +2.5kg — topped rep range last time"`
  - `"3 × 12–15; same weight — fell short on set 3 last time"`
  - `"2 × 10; felt too light last session — up to 15kg"`


-----------------

Do not write commands such as this:    cat "/home/ioan/.claude/projects/-home-ioan-Documents-repos-hevy/ef199773-283f-xxxx-bc35-6c3xxeb57cae/tool-results/toolu_013LcmUKiFQunxxxxJNJaL77.txt" | python3 -c "import sys,json; data=json.load(sys.stdin); text=data[0]['text'];
   workouts=json.loads(text); [print(json.dumps(w, indent=2)) for w in workouts if w['title'] in ('Day A', 'Day B', 'Day C')][:3]"

-----------------