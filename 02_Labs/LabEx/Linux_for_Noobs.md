# LabEx – Linux for Noobs

Status: In Progress  
Documenting labs as they are completed.

---

## Getting Started with Linux

Navigated through the filesystem and verified current working directory.

```bash
pwd
ls
cd
```

Confirmed how directory navigation works and how to move between locations using relative and absolute paths.

---

## Create Personalized Terminal Greeting

Modified shell configuration to display a custom message on terminal start.

Worked with:

```bash
echo
nano ~/.bashrc
```

Understood how `.bashrc` affects terminal behavior and how changes apply after reloading the shell.

---

## Basic File Operations in Linux

Created and managed files.

```bash
touch file1.txt
cp file1.txt copy.txt
ls -l
```

Verified file creation and copying using long listing format.

---

## Get Help on Linux Commands

Explored built-in help systems.

```bash
man ls
ls --help
whatis ls
```

Learned how to read command documentation and understand flags/options.

---

## Delete and Move Files

Practiced safe deletion and file relocation.

```bash
mv file1.txt newfile.txt
rm newfile.txt
```

Confirmed changes using `ls` after each operation.

---

## Linux User Group and File Permissions

Inspected file permissions and group structure.

```bash
ls -l
chmod 755 file1.txt
```

Observed how permission bits change and how they affect file access.

---

## Add New User and Group

Created and managed user accounts.

```bash
useradd testuser
passwd testuser
groupadd testgroup
usermod -aG testgroup testuser
```

Understood how users and groups are structured in Linux.

---

## File and Directory Operations

Worked with directory creation and removal.

```bash
mkdir project
rmdir project
```

Verified directory operations and structure using `ls`.

---

## Find a File

Located files within the system.

```bash
find . -name file1.txt
find / -type f -name "*.txt" 2>/dev/null
```

Learned how to search for files by name and filter results while suppressing permission errors.

---

## Current Focus

Strengthening understanding of:

- File navigation
- Permissions and ownership
- User and group management
- File search and inspection
