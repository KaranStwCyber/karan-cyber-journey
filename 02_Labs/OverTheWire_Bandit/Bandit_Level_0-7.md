## Level 0 → 1

Connected to the Bandit server using SSH on a custom port.

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

First time working inside a remote Linux machine instead of my local system.

---

## Level 1 → 2

There was a file named `-`.  
Normal `cat -` didn’t work because `-` is treated specially.

```bash
cat ./-
```

Using `./` avoids shell misinterpretation.

---

## Level 2 → 3

The filename contained spaces.

```bash
cat "spaces in this filename"
```

The shell splits arguments on spaces, so quotes are necessary.

---

## Level 3 → 4

Had to find a hidden file.

```bash
ls -a
cat .hidden
```

Started checking hidden files by default after this level.

---

## Level 4 → 5

Multiple files were present, but only one was human-readable.

```bash
file ./*
cat <filename>
```

Used `file` to identify the correct file before opening it.

---

## Level 5 → 6

The target file had a specific size and was not executable.

```bash
find . -type f -size 1033c
```

First proper use of `find` with filters.

---

## Level 6 → 7

The file was located somewhere on the system with a specific user and group.

```bash
find / -user bandit7 -group bandit6 2>/dev/null
```

Used `2>/dev/null` to suppress permission errors.
