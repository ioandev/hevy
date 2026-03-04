First, ask me: **"Which day are you training? (A, B, or C)"** — wait for my answer before continuing.

Once I answer, load the corresponding routine from the `routines/` folder:
- Day A → `routines/day-A.md`
- Day B → `routines/day-B.md`
- Day C → `routines/day-C.md`

The routine file defines the exercises, target rep ranges, and muscle focus for that day. Use it as the blueprint — these are the exercises to program, in order.

Then fetch two things using MCP:
1. **My last workout for that day** (search recent workouts for the matching day) — to get actual sets, reps, RPE, weights performed, and any notes I left on exercises. **Exercise notes take high priority** — if I noted why I used a lighter weight, flagged something to change, or said what I want next time, honour that directly in the next session.
2. **The most recent Hevy routine for that day** (use `get-routines`, find the most recent "Day X" routine by date in the name) — to see what was planned for that session.

**Before proposing the next session**, compare the last workout against the routine that was active for it and give a brief performance summary. For each exercise, note whether targets were hit, exceeded, or missed — and if I left a note on an exercise, include it and explain how it influenced the next session. Use this to give honest, specific feedback — e.g. "You hit all your bench targets", "You fell 2 reps short on lat pulldowns on the last set — consider staying at this weight", "You noted the dumbbells felt too light — going up next session". End with an overall verdict on how the session went.

Then propose the next session, and only after that ask: **"Happy with this, or want any changes?"**

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

Output format:
- Exercise name
- Sets × Reps (with weight)
- Any changes from last session, noted with the reason (e.g., "+1 set — hit all reps last time" or "+2.5kg — topped out rep range")

Example output:
```
Here's your next Day A session, based on today's workout:
  ---             
  Bench Press (Barbell)
  4 × 6–8 @ 27.5kg
  +2.5kg — hit 4×8 (top of range) across all sets
  Before: 4x8 @ 25kg
  
  ---
  Lat Pulldown (Cable)
  3 × 8–10 @ 29kg
  +2.5kg — hit 3×10 at RPE 6 across the board, lots of room left
  Before: 1x10 @ 25kg, 1x10 @25kg, 1x5 @25kg
```

Note: The second lines for each exercise are a faded colour in the console.

After outputting the workout, ask: **"Happy with this, or want any changes?"**

- If they want changes, apply them and ask again.
- Once they're happy, ask: **"Should I create a new routine in Hevy?"**
- If yes, fetch the existing routine using `get-routines` to find the matching Day X routine, then call `create-routine` with the new exercises and sets. The name of the routine should be "Day X - DAY/MONTH". Use the `exerciseTemplateId` values already seen in the last workout data — no need to look them up again. Set `reps` and `repRange: {start: reps, end: reps}` to the target rep count. Set `weightKg` to the target weight. For half-rep finisher sets, add them as additional sets with `reps` set to the target half-rep count.

  **Always populate the notes field for every exercise** — never leave it blank. The note should be a compact summary useful at-a-glance during the session. Include: sets × rep range, any half-rep instructions, and a short cue about progression or intent. Examples:
  - `"3 × 8–10; last set + 3 half reps (bottom); progressed from 25kg"`
  - `"4 × 6–8; +2.5kg — topped rep range last time"`
  - `"3 × 12–15; same weight — fell short on set 3 last time"`
  - `"2 × 10; felt too light last session — up to 15kg"`


-----------------

Do not write commands such as this:    cat "/home/ioan/.claude/projects/-home-ioan-Documents-repos-hevy/ef199773-283f-xxxx-bc35-6c3xxeb57cae/tool-results/toolu_013LcmUKiFQunxxxxJNJaL77.txt" | python3 -c "import sys,json; data=json.load(sys.stdin); text=data[0]['text'];
   workouts=json.loads(text); [print(json.dumps(w, indent=2)) for w in workouts if w['title'] in ('Day A', 'Day B', 'Day C')][:3]"

-----------------