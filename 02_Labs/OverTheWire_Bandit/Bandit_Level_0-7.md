Level 0 → 1

Connected to the Bandit server using SSH on a custom port.

ssh bandit0@bandit.labs.overthewire.org -p 2220


First time working inside a remote Linux machine instead of my local system.

Level 1 → 2

There was a file named -.
Normal cat - didn’t work because - is treated specially.

Used:

cat ./-


Learned how relative paths help avoid shell confusion.

Level 2 → 3

Filename had spaces in it.

Used quotes to read it:

cat "spaces in this filename"


Good reminder that the shell splits arguments on spaces.

Level 3 → 4

Had to find a hidden file.

ls -a
cat .hidden


Started checking hidden files by default after this.

Level 4 → 5

Multiple files were present, only one was readable.

file ./*
cat <filename>


Used file to identify which one made sense before opening it.

Level 5 → 6

The file had specific size and wasn’t executable.

find . -type f -size 1033c


First proper use of find with filters.

Level 6 → 7

The file was somewhere on the system with specific owner and group.

find / -user bandit7 -group bandit6 2>/dev/null


Also learned to suppress permission errors using 2>/dev/null.
