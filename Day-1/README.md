# Day 1 — CLI To-Do Manager

A terminal to-do list that survives restarts.

## Features
- Add, show, complete, delete, update tasks
- Persists to `todo_list.json` between runs
- Numbered display with `[x]` / `[ ]` markers
- Range guards and `ValueError` handling on every numeric input

## Run
```bash
python Todo_list.py
```

## Data structure
```python
[
    {"task": "work", "done": False},
    {"task": "gym",  "done": True}
]
```

## What I learned
- `input()` always returns a string — convert before using as an index
- A dict keyed by task name can't support ordering or duplicates; a list of dicts can
- **When the same bug survives three rewrites, the data structure is wrong — patching won't save it**
- Save after every change, not at exit — a crash shouldn't cost data
- An `except` that catches an error but lets execution continue is worse than no `except` — use `continue`
