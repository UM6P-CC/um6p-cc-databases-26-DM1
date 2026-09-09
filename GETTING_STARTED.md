# Run the lab on your computer

This page is for **Lab 0**. You can check your SQL here before you submit, so you do not have to wait for GitHub each time.

You need three things:

1. Python
2. MySQL (the database)
3. A few Python packages from this repo

Already have one of them? Skip that section.

Run every command from **this project folder** (the folder that contains `GETTING_STARTED.md` and `tests`).

---

## 0. Open a terminal in this folder

**Mac:** open **Terminal**. Then:

```bash
cd path/to/um6p-cc-databases-26-DM1
```

**Windows:** open **PowerShell**. Then:

```powershell
cd path\to\um6p-cc-databases-26-DM1
```

Replace the path with wherever you cloned the repo. In Cursor / VS Code you can also use **Terminal → New Terminal**, which usually opens in the project folder already.

---

## 1. Install Python

Skip this if `python3 --version` (Mac) or `py --version` (Windows) already prints a version **3.10 or newer**.

### Mac

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download and install the latest Python 3
3. Check:

```bash
python3 --version
```

### Windows

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Run the installer
3. Tick **Add python.exe to PATH**
4. Check:

```powershell
py --version
```

---

## 2. Install and start MySQL

Skip this if MySQL is already installed, **running**, and the `root` password is `root`.

The tests connect to:

- host: `127.0.0.1`
- user: `root`
- password: `root`
- port: `3306`

Set the root password to **`root`** during install. Leave the port at **3306**.

You only need **MySQL Server**. You do not need Workbench or other extra tools.

### Mac — official installer

1. Go to [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
2. Choose **macOS**, then download **MySQL Community Server**
   - Apple silicon (M1 / M2 / M3 / M4): the **ARM** package
   - Intel Mac: the **x86** package
3. Open the downloaded file and follow the installer
4. When it asks for the **root password**, type `root`
5. Start the server:
   - Open **System Settings** (or **System Preferences**)
   - Click **MySQL**
   - Click **Start MySQL Server**
   - Optional: tick the box so it starts when your Mac starts

If you already use **Homebrew**, you can install it this way instead:

```bash
brew install mysql
brew services start mysql
mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';"
```

(Homebrew MySQL often starts with no password. The last command sets it to `root`.)

### Windows — official installer

1. Go to [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)
2. Download **MySQL Installer for Windows** and run it
3. Choose **Server only** (or **Custom** and pick only **MySQL Server**)
4. Leave the port at **3306**
5. When it asks for the **root password**, type `root`
6. Leave **Start the MySQL Server at System Startup** checked
7. Finish the setup

To check it is running later: search for **Services**, find **MySQL**, status should be **Running**. If it is Stopped, click **Start**.

### After a reboot

MySQL must be running before you run the tests.

- **Mac:** System Settings → **MySQL** → **Start MySQL Server** (or `brew services start mysql` if you used Homebrew)
- **Windows:** Services → **MySQL** → **Start**

If your password is not `root`, see [If the tests cannot connect](#if-the-tests-cannot-connect).

---

## 3. Install the Python packages

Do this once per machine (or again if you delete the `.venv` folder).

This creates a private folder (`.venv`) for this lab so nothing else on your computer is changed.

**Mac:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r tests/requirements.txt
```

**Windows:**

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r tests/requirements.txt
```

Optional — check that Python can reach MySQL:

**Mac:**

```bash
.venv/bin/python -c "import pymysql; pymysql.connect(host='127.0.0.1', user='root', password='root'); print('MySQL is OK')"
```

**Windows:**

```powershell
.venv\Scripts\python.exe -c "import pymysql; pymysql.connect(host='127.0.0.1', user='root', password='root'); print('MySQL is OK')"
```

If that prints `MySQL is OK`, you are ready. If it errors, see [If the tests cannot connect](#if-the-tests-cannot-connect).

---

## 4. Write your answers

Open `tests/test_lab0.py`.

For each exercise, put your SQL **only** inside the quotes:

```python
sql = """
-- WRITE YOUR SQL HERE
"""
```

Do not rename tests or change the code around the SQL.

---

## 5. Run the tests

**Mac:**

```bash
.venv/bin/python -m pytest tests/test_lab0.py -v
```

**Windows:**

```powershell
.venv\Scripts\python.exe -m pytest tests/test_lab0.py -v
```

Read the output:

- `PASSED` — that exercise is correct
- `FAILED` — fix that SQL and run the same command again

Each run starts from a clean `LibraryDB`, so you can run the tests as many times as you want.

Run **all** tests, not one at a time. Later tests need the tables and data from earlier ones.

---

## 6. Submit when you are ready

Local tests are for you. The grade still comes from GitHub:

```bash
gh student submit
```

Then check the **Actions** tab on your repo.

---

## If the tests cannot connect

Typical message: `Can't connect to MySQL` or `Access denied`.

1. Is MySQL **running**? (Mac: System Settings → MySQL. Windows: Services → MySQL.)
2. Did you set the root password to `root` and leave the port at `3306`?
3. If your password is not `root`, set it only in that terminal, then run the tests again:

**Mac:**

```bash
export MYSQL_PASSWORD='your-password'
.venv/bin/python -m pytest tests/test_lab0.py -v
```

**Windows (PowerShell):**

```powershell
$env:MYSQL_PASSWORD="your-password"
.venv\Scripts\python.exe -m pytest tests/test_lab0.py -v
```

Optional: `MYSQL_HOST` (default `127.0.0.1`), `MYSQL_USER` (default `root`), `MYSQL_PORT` (default `3306`).

4. `python3` / `py` not found → go back to [Install Python](#1-install-python). Tick **Add python.exe to PATH** on Windows, then open a **new** terminal.
5. `pytest` not found → you skipped step 3, or you are not using `.venv/.../python` as in step 5.

---

## Commands cheat sheet

| What | Mac | Windows |
| --- | --- | --- |
| Start MySQL | System Settings → MySQL → Start (or `brew services start mysql`) | Services → MySQL → Start |
| Install packages (once) | `python3 -m venv .venv` then `.venv/bin/python -m pip install -r tests/requirements.txt` | `py -m venv .venv` then `.venv\Scripts\python.exe -m pip install -r tests/requirements.txt` |
| Run tests | `.venv/bin/python -m pytest tests/test_lab0.py -v` | `.venv\Scripts\python.exe -m pytest tests/test_lab0.py -v` |
