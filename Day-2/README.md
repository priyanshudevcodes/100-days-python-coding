# Day 2 — Password Generator + Strength Analyzer

Terminal password tool: generates cryptographically secure passwords and scores any password 0–100.

## Features
- Generator with user-defined length, letter/digit/symbol counts
- Uses `secrets` (not `random`) — cryptographically secure randomness
- Retry-loop generation until all requirements are met
- Analyzer scores via regex checks + length, prints ✓/✗ report
- `rich` for colored terminal output

## Run
```bash
pip install rich
python password_tool.py
```

## Scoring (total 100)
| Check | Points |
|---|---|
| lowercase present | +8 |
| uppercase present | +8 |
| digit present | +15 |
| symbol present | +22 |
| length ≥ 12 | +47 |
| length < 12 | −5 |

Verdict: ≥75 Strong · ≥45 Medium · else Weak.
Length carries the most weight — a long simple password beats a short complex one.

## What I learned
- `random` is predictable (seeded formula); `secrets` pulls OS entropy — games vs security
- `any()` returns a bool; `sum()` over booleans counts — `True >= 3` is `1 >= 3`, silently False
- Regex ranges: `[A-a]` is not `[A-Za-z]` — character ranges follow ASCII order
- In if/elif chains, first match wins — order tiers from biggest down or branches go dead
- Two checks measuring the same thing (display vs scoring) must use the same comparison
