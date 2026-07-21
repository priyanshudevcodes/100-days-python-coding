# Build Log

## Day 1 — CLI To-Do Manager
- **Built:** to-do manager with JSON persistence, 6 operations, input guards
- **Broke:** used a dict instead of a list of dicts — cost 3 rewrites; except without continue fell through
- **Learned:** input() returns str; fix the data structure, don't patch around it

## Day 2 — Password Generator + Strength Analyzer
- **Built:** secure generator (secrets) + regex 0–100 analyzer, rich colors
- **Broke:** any() vs sum() froze the generator; elif chained length onto symbol check; > vs >= at boundary
- **Learned:** bool-vs-int type confusion is my repeating pattern — check both sides of every comparison
