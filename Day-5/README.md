# Day 5 — Typing Speed Tester

Measures typing speed in WPM and word-level accuracy against a random target sentence.

## Features
- Random sentence from a pool
- High-precision timing with `time.perf_counter()`
- WPM using the standard 5-characters-per-word convention
- Word-level accuracy via `zip` over split word lists

## Run
```bash
python typing_tester.py
```

## Design notes
- **WPM** = (characters ÷ 5) ÷ minutes — the industry-standard formula
- **Accuracy** is word-level, not character-level. Character comparison misaligns after a single insertion or deletion, so one early typo can drop accuracy near zero. Word comparison isolates each error.
- Accuracy denominator is the *target* word count, so typing only part of the sentence is correctly penalized
- Comparison is case- and punctuation-sensitive: `"dog"` ≠ `"dog."` — strict by design

## What I learned
- `time.perf_counter()` is the correct stopwatch for durations; `time.time()` is for wall-clock dates
- `zip` on strings iterates characters; on lists it iterates elements — `.split()` changes the whole meaning
- `zip` stops at the shorter sequence, so the denominator choice determines whether partial input is penalized
- Guard every division against zero even when it "can't" happen