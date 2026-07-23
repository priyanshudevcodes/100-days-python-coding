# Build Log

## Day 1 — CLI To-Do Manager
- **Built:** to-do manager with JSON persistence, 6 operations, input guards
- **Broke:** used a dict instead of a list of dicts — cost 3 rewrites; except without continue fell through
- **Learned:** input() returns str; fix the data structure, don't patch around it

## Day 2 — Password Generator + Strength Analyzer
- **Built:** secure generator (secrets) + regex 0–100 analyzer, rich colors
- **Broke:** any() vs sum() froze the generator; elif chained length onto symbol check; > vs >= at boundary
- **Learned:** bool-vs-int type confusion is my repeating pattern — check both sides of every comparison

## Day 3 — File Organizer
- **Built:** menu-driven organizer, sorts files by extension into category folders
- **Broke:** shutil.move renamed files when destination didn't exist — lost test PDFs; rglob re-found moved files; globbed the wrong folder
- **Learned:** mkdir before move, always; glob vs rglob; test destructive code on junk files

## Day 4 — Number System Converter + Bitwise Playground
- **Built:** d/b/h converter + bitwise playground with bit-aligned output
- **Broke:** except-without-continue again (4th time) — crashed on bad bitwise input
- **Learned:** f-string format specs beat bin()/hex(); reflex — every except, ask "should code below still run?"

## Day 5 — Typing Speed Tester
- **Built:** WPM + accuracy tester with perf_counter timing and random sentence pool
- **Broke:** zipped strings instead of word lists — one typo tanked accuracy to ~10%; \2 instead of \n2
- **Learned:** zip granularity depends on what you feed it; character vs word comparison is a real design decision