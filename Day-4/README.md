# Day 4 — Number System Converter + Bitwise Playground

Converts between decimal, binary, and hexadecimal, and visualizes bitwise operations.

## Features
- Convert d ↔ b ↔ h in any direction
- Bitwise playground: AND, OR, XOR, left/right shift
- Bit-aligned output so the operations are visually clear

## Run
```bash
pip install rich
python number_converter.py
```

## Bitwise notes
`5 << 1 = 10` — shifting left adds a zero on the right (`0101` → `1010`), doubling the value. Each left shift is ×2, each right shift is ÷2. This is how hardware registers and GPIO pins are manipulated.

## What I learned
- f-string format specs: `{n:b}` binary, `{n:x}` hex, `{n:04b}` zero-padded — no prefix stripping needed
- `int("1010", 2)` and `int("FF", 16)` — the base argument parses strings
- `input()` never raises; the `int(x, base)` conversion does — the guard must wrap the conversion
- Every `except` needs `continue` if the code below depends on the failed value