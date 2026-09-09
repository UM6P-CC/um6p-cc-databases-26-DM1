# Data Management Labs 

## 1. Getting started with a lab

1. **Accept the assignment** using the link/command your instructor shares.
2. **Clone your repository** to your own computer.
3. **Run the tests on your computer** (recommended) so you can check your SQL before you submit. Follow [GETTING_STARTED.md](GETTING_STARTED.md). It starts from zero (Python, database, how to run tests). Skip any step you already have.
4. **Write your answers** in the location specified for that lab (see below).
5. Save your work then run:
   ```
   gh student submit
   ```
6. Check the **Actions** tab of your repo to see your grading results.

If Python and MySQL (`root` / `root` on port 3306) are already set up:

```
python3 -m pip install -r tests/requirements.txt
python3 -m pytest tests/test_lab0.py -v
```

On Windows, use `py` instead of `python3`. Full commands for Mac and Windows are in [GETTING_STARTED.md](GETTING_STARTED.md).

## 2. Where to write your answers

- **Most labs:** open `tests/test_labN.py` (e.g. `test_lab0.py`, `test_lab3.py`) and fill in each blank:
  ```python
  sql = """
  -- WRITE YOUR SQL HERE
  """
  ```
  Write your SQL directly inside the triple quotes. Do not rename, delete, or restructure the surrounding test code ,only edit the SQL inside each block.
  
## 3. Starting from Lab 3: how grading works

From Lab 3 onward, each lab includes a schema and a populated dataset that your queries run against:
- **Lab 3** → `seed.sql`
- **Lab 4** → `lab4_seed.sql`
- **Lab 5** → `lab5_seed.sql`

These files are already in your repo, you can look at the data directly to understand what you're querying.
**Important:** Your SQL is also tested using a hidden dataset. Therefore, write general SQL queries that solve the question. Do not write queries that only match the specific values in the visible dataset.


## 4. Submitting

```
gh student submit
```

You can submit multiple times, each submission is graded independently, and your most recent submission is what counts. Check the **Actions** tab after each submission to see your score and any failure details.

