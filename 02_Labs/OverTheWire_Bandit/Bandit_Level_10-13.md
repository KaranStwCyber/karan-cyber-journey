# OverTheWire Bandit (Level 10–13)

---

## Level 10 → 11

Opened `data.txt`. It didn’t look readable, but the format looked like base64 (letters, numbers, ending with `=`).

Decoded it:

```bash
base64 -d data.txt
```

Got the password.

Nothing complicated. Just needed to recognize base64.

---

## Level 11 → 12

Hint said letters were rotated by 13 positions.

That’s ROT13.

Checked the file — text was readable but scrambled.

Used:

```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

That decoded it and showed the password.

Simple substitution. Good use of `tr`.

---

## Level 12 → 13

File looked like random data.

Instead of guessing, I checked the type:

```bash
file data.txt
```

It showed compression.

After extracting, it was compressed again in another format.

So I kept repeating:
- check file type
- rename if needed
- extract

Commands used during the process:

```bash
gunzip
bunzip2
tar -xvf
file
```

---

## Level 13 → 14

This time there was no password in a file. There was an SSH private key.

Logged in using:

```bash
ssh -i sshkey.private bandit14@localhost -p 2220
```

Got a permission error first.

Fixed it:

```bash
chmod 600 sshkey.private
```

Then login worked and I got the next password.
