First, ask me: **"Which day are you training? (A, B, or C)"** — wait for my answer before continuing.

Once I answer, load the corresponding routine from the `routines/` folder:
- Day A → `routines/day-A.md`
- Day B → `routines/day-B.md`
- Day C → `routines/day-C.md`

The routine file defines the exercises, target rep ranges, and muscle focus for that day. Use it as the blueprint — these are the exercises to program, in order.

Then fetch my last workout for that day using MCP (search recent workouts for the matching day) to get actual sets, reps, RPE, and weights performed.

Follow these progression rules:

1. **Progressive overload priority:** Increase volume (sets/reps) first. Only increase weight once I've hit the top of the rep range across all sets.
2. **Don't stall me:** If I missed a target by just 1 rep on one set but hit everything else, still progress me — don't hold me back for a minor miss.
3. **Half reps as finishers:** For isolation exercises (e.g., curls, lateral raises, flyes), add a set of half reps at the end to maximize time under tension. Don't add half reps to heavy compound lifts.
4. **Cap weight jumps at 25% of current load:** When increasing weight, the increment must not exceed 25% of the current working weight. If the next available dumbbell/plate increment would exceed this (e.g. 2.5kg → 5kg is a 100% jump), do NOT increase weight — keep the same weight and note the rep ceiling was hit, or add a set instead.

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
- If yes, fetch the existing routine using `get-routines` to find the matching Day X routine, then call `creatine-routine` with the new exercises and sets. The name of the routine should be "Day X - DAY/MONTH". Use the `exerciseTemplateId` values already seen in the last workout data — no need to look them up again. Set `reps` and `repRange: {start: reps, end: reps}` to the target rep count. Set `weightKg` to the target weight. For half-rep finisher sets, add them as additional sets with `reps` set to the target half-rep count. Mention in the notes "Last X sets are half reps"


-----------------

Do not write commands such as this:    cat "/home/ioan/.claude/projects/-home-ioan-Documents-repos-hevy/ef199773-283f-xxxx-bc35-6c3xxeb57cae/tool-results/toolu_013LcmUKiFQunxxxxJNJaL77.txt" | python3 -c "import sys,json; data=json.load(sys.stdin); text=data[0]['text'];
   workouts=json.loads(text); [print(json.dumps(w, indent=2)) for w in workouts if w['title'] in ('Day A', 'Day B', 'Day C')][:3]"

-----------------