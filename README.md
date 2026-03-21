# Hevy AI Coach

Your personal strength coach, powered by Claude Code and the [Hevy](https://hevy.com) workout tracker.

This repo replaces the guesswork in your training with an AI that reads your actual performance data, applies proven progression logic, and writes your next session directly into Hevy — no spreadsheet, no coach, no monthly fee (other than Hevy itself).

## What it does

You finish a workout. You open your terminal and type `/generate-next`. Claude:

1. **Pulls your last session** from Hevy — every set, rep, weight, and note you logged.
2. **Compares it against the routine** that was planned for that day.
3. **Gives you honest feedback** — what you hit, what you missed, and why.
4. **Programs your next session** using real progressive overload rules: volume before load, capped weight jumps (never more than 25% increase), partial-rep finishers on isolation work, and smart deloading when you stall.
5. **Pushes the new routine to Hevy** so it's waiting for you when you walk into the gym.

It also handles scheduling. Type `/reschedule` and it figures out your next training dates based on your Mon/Wed/Fri rotation and renames your Hevy routines to match.

## How it works

There's no app to install. The entire system is a set of markdown files and AI coding agent commands. It's built for Claude Code, but the heavy lifting is in the markdown — the routines, the progression rules, the weight lists. That means you can adapt it for **Cursor, GitHub Copilot, Codex, or any agent that can read markdown and call an MCP server**. Most of the work is already done for you.

```
routines/          # Your training programs (Day A, B, C)
weights.md         # Available equipment weights at your gym
CLAUDE.md          # The rules Claude follows (progression, warm-ups, rest, partials)
.claude/commands/  # Slash commands: /generate-next, /reschedule
.mcp.json          # Hevy MCP server connection
scripts/           # Utility scripts (table formatting)
```

The magic is in `CLAUDE.md` — it codifies the training principles a good coach would follow:

- **Progressive overload** — increase reps first, then weight, only when you've earned it.
- **Smart weight selection** — picks from the actual plates and cables available at your gym.
- **Warm-up protocols** — percentage-based warm-up sets for compounds, skip warm-ups when muscles are already primed.
- **Rest periods** — longer rest for heavy compounds (2.5-3.5 min), shorter for isolation (45-90 sec). No shortcuts.
- **Partial reps** — controlled half-rep finishers on the last set of isolation exercises, with specific ROM cues per movement.
- **Staleness detection** — checks if the routine was already updated before regenerating, so you don't lose manual tweaks.

## Getting started

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed
- A [Hevy](https://hevy.com) account (Pro)
- [hevy-mcp](https://github.com/jamesawgill/hevy-mcp) server set up with your Hevy API key

### Setup

1. **Fork this repo** and clone it locally.

2. **Edit `weights.md`** with the actual weights available at your gym — cable stack increments, barbell plates, dumbbells. This is how Claude knows what weight to prescribe.

3. **Edit the routines** in `routines/` to match your training split. The included Day A/B/C split is a push-pull-legs hybrid, but you can structure it however you want. Use the markdown table format — the column headers tell Claude what to look for.

4. **Configure `.mcp.json`** to point to your hevy-mcp server install and `.env` file with your API key.

5. **Tweak `CLAUDE.md`** — this is where you make it yours:
   - Change workout days from Mon/Wed/Fri to whatever fits your schedule.
   - Adjust progression rules (e.g., allow bigger weight jumps if you're a beginner).
   - Modify rest periods, partial rep policy, or warm-up percentages.
   - Add rules specific to your training style or injuries.

6. **Run it:**
   ```bash
   cd your-hevy-repo
   claude
   # then type: /generate-next
   ```

### Customization ideas

- **Different splits** — PPL, upper/lower, full body, bro split. Just create routine files and update the alternation pattern in CLAUDE.md.
- **Periodization** — Add deload week rules, mesocycle tracking, or RPE-based autoregulation to CLAUDE.md.
- **Injury management** — Add constraints like "never go above 60kg on bench" or "substitute leg press for squats".
- **Multiple gyms** — Create separate `weights-*.md` files for different gyms and tell Claude which one you're at.
- **Training partners** — Fork and customize for each person's progression level and equipment.
- **Different AI agent** — The core logic lives in markdown files, not Claude-specific code. Swap in Cursor, GitHub Copilot, Codex, or any coding agent that supports MCP. Point it at the same routines, weights, and rules — most of the work transfers directly.

## Why this exists

Hiring a coach costs $150-300/month. Most of what they do session-to-session is look at what you lifted last time and make small adjustments. That's exactly what an LLM with access to your training data can do — consistently, instantly, and for free.

The hard part of training isn't knowing the exercises. It's knowing when to add weight, when to add reps, when to back off, and making sure you actually do it. This system handles that.

## License

MIT — take it, change it, make it yours.
