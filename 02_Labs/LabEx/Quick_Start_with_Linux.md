# LabEx – Quick Start with Linux

Completed foundational Linux labs inside an isolated LabEx environment.  
Focus was on practical command usage, file system behavior, and permission control.

---

## 1. Your First Linux Lab

Objective: Navigate the filesystem and identify working directory.

Executed:

```bash
pwd
ls -a
cd /home
```

Verified how absolute paths differ from relative paths and confirmed directory transitions using `pwd`.

---

## 2. Display User and Group Information

Objective: Inspect current user identity and group associations.

```bash
whoami
id
groups
```

Observed UID, primary group, and supplementary groups.  
Understood how Linux uses UID/GID for permission decisions.

---

## 3. Basic File Operations

Objective: Create, duplicate, move, and delete files safely.

```bash
touch file1.txt
cp file1.txt backup.txt
mv backup.txt archive.txt
rm archive.txt
```

Validated each operation using `ls -l` to confirm file state changes.

---

## 4. Files and Directories

Objective: Work with nested directories and inspect metadata.

```bash
mkdir project
cd project
mkdir src
ls -l
```

Analyzed permission bits and ownership fields in long listing format.

---

## 5. File Contents and Comparing

Objective: Inspect file content and detect differences.

```bash
cat file1.txt
head file1.txt
tail file1.txt
diff file1.txt file2.txt
```

Understood how `diff` identifies line-level changes between files.

---

## 6. The Manuscript Mystery

Objective: Locate hidden or misplaced files within directory tree.

Applied navigation and file inspection techniques to extract required content.

Reinforced enumeration mindset: list → inspect → narrow down.

---

## 7. Permissions of Files

Objective: Modify and verify permission settings.

```bash
ls -l file1.txt
chmod 644 file1.txt
chmod 755 file1.txt
```

Observed how read/write/execute bits affect accessibility.

---

## 8. Change File Ownership

Objective: Modify ownership for controlled access.

```bash
chown user1 file1.txt
chgrp group1 file1.txt
```

Verified ownership updates via `ls -l` and analyzed impact on access control.

---

## 9. User Account Management

Objective: Create and manage temporary user accounts.

```bash
useradd testuser
passwd testuser
usermod -aG sudo testuser
userdel testuser
```

Observed how users and groups integrate with file permissions.

---

## 10. The Joker's Trick

Objective: Solve a restricted-access scenario using permission logic.

Applied a combination of ownership modification and permission adjustment to gain required access.

Demonstrated understanding of:

- User identity
- Group membership
- Permission bits
- Access inheritance
