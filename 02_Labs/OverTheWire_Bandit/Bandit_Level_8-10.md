## Level 7 → 8

The password was inside `data.txt` and the hint mentioned the word **"millionth"**.  
Instead of reading the whole file manually, I searched directly for the keyword.

```bash
grep millionth data.txt
```

Started getting more comfortable using `grep` instead of manually checking files.

---

## Level 8 → 9

The file had many repeated lines and only one unique line.

At first I tried `uniq` directly, then realized it requires sorted input.

```bash
sort data.txt | uniq -u
```

Good reminder that command order matters in Linux pipelines.

---

## Level 9 → 10

The file looked unreadable when opened normally.

Used:

```bash
strings data.txt | grep "="
```

This worked.

Not every file should be viewed using `cat`.  
Sometimes you need to extract readable content first.

