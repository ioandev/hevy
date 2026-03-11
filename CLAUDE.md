# Hevy MCP — Quick Reference

The `hevy-mcp` MCP server is configured in `.mcp.json`. Call its tools **directly** — never spawn an agent just to use them.

## Available Tools

### Workouts
- `get-workouts` — paginated list, newest first (`page`, `pageSize`)
- `get-workout` — single workout by ID
- `get-workout-count` — total workout count
- `get-workout-events` — changes since a given date
- `create-workout` — create a new workout
- `update-workout` — update an existing workout

### Routines
- `get-routines` — paginated list
- `get-routine` — single routine by ID
- `create-routine` — create a routine
- `update-routine` — update a routine

### Exercise Templates
- `get-exercise-templates` — paginated list
- `get-exercise-template` — single template by ID
- `get-exercise-history` — history for a template
- `create-exercise-template` — create a custom template

### Routine Folders
- `get-routine-folders` — list folders
- `get-routine-folder` — single folder by ID
- `create-routine-folder` — create a folder

### Webhooks
- `get-webhook-subscription`
- `create-webhook-subscription`
- `delete-webhook-subscription`

## Usage Rules
- Call tools directly — no agents, no exploration loops.
- **Always use `pageSize: 4`** for all paginated tool calls — never higher, unless it's for get workouts in which case use **`pageSize: 6`**.
- For "last workout": `get-workouts` with `page=1, pageSize=1`.
- For editing a template: `get-exercise-template` by ID, then `create-exercise-template` or update as needed.
- Never call more tools than necessary to answer the question.

## Known Gotchas

### repRange must always have start=end, set correctly on first write
The `repRange` field is required by the API but the Hevy app uses an internal `input_modifier` field to control reps display. Key rules:
- Always set `repRange: {start: reps, end: reps}` — matching the `reps` value exactly.
- **Never** send `repRange` with `start ≠ end` (e.g. `{start:6, end:8}`). This locks the exercise into "range mode" on first write and subsequent updates cannot fix it — reps will show blank forever in that routine.
- If an exercise is already broken (was first written with mismatched start/end), **create a new routine** from scratch. Updating in place won't repair it.
- For "X+" targets (e.g. "13+"), use `repRange: {start:13, end:13}`.
- The API has no delete endpoint — routines must be deleted manually in the app.
