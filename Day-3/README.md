# Day 3 — File Organizer

Menu-driven tool that sorts files in a folder into category subfolders by extension.

## Features
- View all files with their extensions
- Organize by extension: `.pdf` → Documents, `.jpg` → Images, `.mp3` → Audio, `.py` → Python Programmes
- Creates destination folders automatically
- Skips files that already exist at the destination
- Skips the script itself

## Run
```bash
pip install rich
python file-manager.py
```

Place your messy files in a subfolder next to the script, then enter that folder's name when prompted.

## What I learned
- `shutil.move()` to a non-existent folder silently **renames** the file to that path — destroyed test files before adding `mkdir`
- `glob` searches one folder; `rglob` recurses — rglob re-found already-moved files and crashed
- Always `mkdir(parents=True, exist_ok=True)` before any move
- `__file__` is a full path; compare with `Path(__file__).name`
- Test destructive file operations on junk files, never real folders

## Known limits
- Four repeated per-extension blocks (dict-based refactor planned for a later project)
- Only four extensions supported
