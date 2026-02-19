# OverTheWire Bandit (Level 10–13)

---

## Level 10 → 11

Opened `data.txt`. It didn’t look readable, but the format looked like base64  
(letters, numbers, ending with `=`).

Decoded it:

```bash
base64 -d data.txt
Got the password.

Nothing complicated. Just needed to recognize base64.

Level 11 → 12
Hint said letters were rotated by 13 positions.

That’s ROT13.

Checked the file — text was readable but scrambled.

Used:

cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
That decoded it and showed the password.

Simple substitution. Good use of tr.

Level 12 → 13
File looked like random data.

Instead of guessing, I checked the type:

file data.txt
It showed compression.

After extracting, it was compressed again in another format.
So I kept repeating
