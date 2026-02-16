OverTheWire Bandit – Levels 0 to 7

I started Bandit to strengthen my Linux command-line fundamentals and get comfortable working inside a remote terminal environment.

Each level required small but precise command-line thinking. Below is a summary of what I practiced.

Level 0 → 1

The first step was connecting to the remote machine using SSH with a custom port.

Command used:

ssh bandit0@bandit.labs.overthewire.org -p 2220


This helped me understand how remote login works and how non-default ports are specified.

Level 1 → 2

The task involved reading a file named "-". Since "-" is treated specially in Linux, using it directly caused issues.

Command used:

cat ./-


This reinforced how Linux interprets special characters and why relative paths matter.

Level 2 → 3

The challenge involved a filename containing spaces.

Command used:

cat "spaces in this filename"


This improved my understanding of quoting and how the shell parses arguments.

Level 3 → 4

The objective was to find a hidden file.

Command used:

ls -a
cat .hidden


This introduced hidden files and the importance of enumeration in Linux environments.

Level 4 → 5

Multiple files were present, but only one was human-readable.

Command used:

file ./*
cat <filename>


This strengthened my understanding of file types and inspection techniques.

Level 5 → 6

The password file had specific properties such as size and permissions.

Commands used:

find . -type f -size 1033c


This level improved my use of the find command with filters.

Level 6 → 7

The file was located somewhere on the system with specific ownership.

Commands used:

find / -user bandit7 -group bandit6 2>/dev/null


This introduced searching across directories while handling permission errors.

What Improved After Level 0–7

Better comfort with SSH
Improved file enumeration skills
Stronger understanding of Linux file handling
Increased confidence navigating terminal environments
