Reschedule upcoming workout routines in Hevy based on the alternating Day A / Day B pattern.

## Inputs

- **User instructions** (optional, passed as `$ARGUMENTS`): e.g. "Tomorrow I will do Day A", "Next session is Day B on Friday". If empty, infer automatically from the last workout.
- **Workout days**: Monday, Wednesday, Friday (fixed).
- **Plans**: Day A and Day B alternate. No Day C unless the user explicitly mentions it.

## Steps

### 1. Fetch data (two calls)

- `get-routines` (page 1, pageSize 4) — find all routines whose title starts with "Day" and does **not** contain "OLD" (case-insensitive). These are the "active" routines.
- `get-workouts` (page 1, pageSize 1) — get the most recent workout to determine what was last done and when.

### 2. Determine the starting point

From the last workout title, extract the day type (A, B, or C) and the date it was performed.

- If `$ARGUMENTS` contains an override (e.g. "Tomorrow I will do Day A"), use that as the next session's day type and date. Resolve relative words like "tomorrow", "Wednesday", etc. against today's date (provided in system context).
- If no override, the next session is the **opposite** day type on the **next workout weekday** after the last workout's date. The alternation is: A → B → A → B …

### 3. Build the schedule

Starting from the determined next session, assign day types to the next workout weekdays, continuing the alternation. Only schedule as many sessions as there are active routines (typically 2: one Day A and one Day B).

Example — if next session is Day A on Wednesday 18 March:
- The Day A routine gets the date 18/3 (Wednesday)
- The Day B routine gets the date 20/3 (Friday)

### 4. Rename the active routines

Each active routine gets renamed with the date of its next scheduled session:

- Title format: `Day X - DD/MM` (e.g. `Day A - 18/3`, `Day B - 20/3`)
- Only the title changes — do **not** modify exercises, sets, weights, notes, or anything else.

### 5. Show the plan and confirm BEFORE doing anything

Print the proposed plan clearly, e.g.:

```
Upcoming schedule (starting Wednesday 18 March):
  Wednesday 18/3 → Day A
  Friday 20/3    → Day B

Routine renames:
  "Day A - 11/3"  →  "Day A - 18/3"
  "Day B - 14/3"  →  "Day B - 20/3"
```

Then ask: **"Should I go ahead?"**

Only proceed with renaming after confirmation.

### 6. Apply changes

Call `update-routine` for each active routine, changing only the `title` field. Pass all exercises through unchanged.

## Rules

- Only touch routines that start with "Day" and do NOT contain "OLD".
- Never rename or modify `-OLD` routines.
- Do not change exercises, sets, weights, or notes — only the title.
- Use `pageSize: 4` for routines, `pageSize: 1` for the last workout (per CLAUDE.md).
