import os

import pymysql
import pytest
import sqlparse


MEMBERS = (
    (1, "Amina", "El Fassi", 20, "Casablanca"),
    (2, "Youssef", "Benali", 21, "Marrakech"),
    (3, "Omar", "Tazi", 23, "Rabat"),
)

BOOKS = (
    (1, "Introduction to Databases", "Databases"),
    (2, "Discrete Mathematics", "Mathematics"),
    (3, "Operating Systems Concepts", "Systems"),
)

LIBRARIANS = (
    (1, "Nadia", "Alami", "Digital Resources"),
    (2, "Karim", "Idrissi", "Circulation"),
    (3, "Laila", "Bennani", "Archives"),
)

LOANS = (
    (1, 1, 1, "January 2026"),
    (2, 2, 2, "January 2026"),
    (3, 3, 3, "February 2026"),
)


def _mysql_connect():
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "127.0.0.1"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "root"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        autocommit=True,
    )


def execute_sql(cur, sql):
    """Run every statement in the student SQL box (comments-only is ignored)."""
    ran_any = False
    for statement in sqlparse.split(sql):
        stripped = statement.strip()
        if not stripped:
            continue
        if not sqlparse.format(stripped, strip_comments=True).strip():
            continue
        cur.execute(stripped)
        ran_any = True
    assert ran_any, "Write your SQL inside the quotes. A comment is not enough."


def show_columns(cur, table):
    cur.execute(f"SHOW COLUMNS FROM `{table}`")
    return {row[0]: row for row in cur.fetchall()}


def assert_table_exists(cur, table):
    cur.execute("SHOW TABLES LIKE %s", (table,))
    assert cur.fetchone() is not None, f"Table {table} was not created"


def assert_schema(cur, table, columns, primary_key, not_null=()):
    assert_table_exists(cur, table)
    cols = show_columns(cur, table)
    assert set(cols) == set(columns), (
        f"{table} columns should be {list(columns)}, got {list(cols)}"
    )
    assert cols[primary_key][3] == "PRI", f"{table}.{primary_key} should be the primary key"
    for column in not_null:
        assert cols[column][2] == "NO", f"{table}.{column} should be NOT NULL"


def assert_row_set(rows, expected, message):
    assert set(rows) == set(expected), message


@pytest.fixture(scope="session", autouse=True)
def reset_database():
    conn = _mysql_connect()
    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS LibraryDB")
    cur.close()
    conn.close()


@pytest.fixture
def connection():
    conn = _mysql_connect()

    yield conn

    conn.close()


@pytest.fixture
def cursor(connection):
    cur = connection.cursor()

    yield cur

    cur.close()


def test_01_create_database(cursor):
    """
    Exercise 1

    Create a database named LibraryDB.
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cursor, sql)

    cursor.execute("""
        SHOW DATABASES LIKE 'LibraryDB'
    """)

    assert cursor.fetchone() is not None, "Database LibraryDB was not created"


def test_02_create_members_table(connection):
    """
    Exercise 2

    Create the Members table with exactly these columns:

    - member_id primary key
    - first_name NOT NULL
    - last_name NOT NULL
    - age
    - city
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    assert_schema(
        cur,
        "Members",
        columns=("member_id", "first_name", "last_name", "age", "city"),
        primary_key="member_id",
        not_null=("first_name", "last_name"),
    )


def test_03_create_books_table(connection):
    """
    Exercise 3

    Create the Books table with exactly these columns:

    - book_id primary key
    - title
    - category
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    assert_schema(
        cur,
        "Books",
        columns=("book_id", "title", "category"),
        primary_key="book_id",
    )


def test_04_create_librarians_table(connection):
    """
    Exercise 4

    Create the Librarians table with exactly these columns:

    - librarian_id primary key
    - first_name
    - last_name
    - section
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    assert_schema(
        cur,
        "Librarians",
        columns=("librarian_id", "first_name", "last_name", "section"),
        primary_key="librarian_id",
    )


def test_05_create_loans_table(connection):
    """
    Exercise 5

    Create the Loans table with exactly these columns:

    - loan_id primary key
    - member_id
    - book_id
    - loan_period

    Do NOT create foreign keys.
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    assert_schema(
        cur,
        "Loans",
        columns=("loan_id", "member_id", "book_id", "loan_period"),
        primary_key="loan_id",
    )

    cur.execute("""
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
        WHERE TABLE_SCHEMA = 'LibraryDB'
          AND LOWER(TABLE_NAME) = 'loans'
          AND CONSTRAINT_TYPE = 'FOREIGN KEY'
    """)
    assert cur.fetchone()[0] == 0, "Loans should not have foreign keys"


def test_06_insert_members(connection):
    """
    Exercise 6

    Insert these three members into Members
    (use these ids, names, ages, and cities):

    1, Amina, El Fassi, 20, Casablanca
    2, Youssef, Benali, 21, Marrakech
    3, Omar, Tazi, 23, Rabat
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    cur.execute("""
        SELECT member_id, first_name, last_name, age, city
        FROM Members
    """)
    assert_row_set(
        cur.fetchall(),
        MEMBERS,
        "Members should contain the three rows listed in the exercise",
    )


def test_07_insert_books(connection):
    """
    Exercise 7

    Insert these three books into Books:

    1, Introduction to Databases, Databases
    2, Discrete Mathematics, Mathematics
    3, Operating Systems Concepts, Systems
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    cur.execute("""
        SELECT book_id, title, category
        FROM Books
    """)
    assert_row_set(
        cur.fetchall(),
        BOOKS,
        "Books should contain the three rows listed in the exercise",
    )


def test_08_insert_librarians(connection):
    """
    Exercise 8

    Insert these three librarians into Librarians.
    Each one belongs to a different section:

    1, Nadia, Alami, Digital Resources
    2, Karim, Idrissi, Circulation
    3, Laila, Bennani, Archives
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    cur.execute("""
        SELECT librarian_id, first_name, last_name, section
        FROM Librarians
    """)
    rows = cur.fetchall()
    assert_row_set(
        rows,
        LIBRARIANS,
        "Librarians should contain the three rows listed in the exercise",
    )
    sections = {row[3] for row in rows}
    assert len(sections) == 3, "Each librarian should belong to a different section"


def test_09_insert_loans(connection):
    """
    Exercise 9

    Insert these three loans into Loans.
    Every loan must have a loan_period:

    1, 1, 1, January 2026
    2, 2, 2, January 2026
    3, 3, 3, February 2026
    """

    sql = """
    -- WRITE YOUR SQL HERE
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")
    execute_sql(cur, sql)

    cur.execute("""
        SELECT loan_id, member_id, book_id, loan_period
        FROM Loans
    """)
    rows = cur.fetchall()
    assert_row_set(
        rows,
        LOANS,
        "Loans should contain the three rows listed in the exercise",
    )
    assert all(row[3] for row in rows), "Every loan must contain a loan_period"


def test_10_list_all_members(connection):
    """
    Query 1

    List all members (all columns).
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    assert_row_set(
        cur.fetchall(),
        MEMBERS,
        "Expected all three members, all columns",
    )


def test_11_list_book_titles(connection):
    """
    Query 2

    List only the book titles.
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    titles = {row[0] for row in cur.fetchall()}
    assert titles == {
        "Introduction to Databases",
        "Discrete Mathematics",
        "Operating Systems Concepts",
    }


def test_12_members_older_than_20(connection):
    """
    Query 3

    Find all members older than 20 (all columns).
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    assert_row_set(
        cur.fetchall(),
        tuple(row for row in MEMBERS if row[3] > 20),
        "Expected the members whose age is greater than 20",
    )


def test_13_librarians_digital_resources(connection):
    """
    Query 4

    Find all librarians in the Digital Resources section (all columns).
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    assert_row_set(
        cur.fetchall(),
        tuple(row for row in LIBRARIANS if row[3] == "Digital Resources"),
        "Expected the librarian in the Digital Resources section",
    )


def test_14_january_loans(connection):
    """
    Query 5

    List all loans that took place in January 2026 (all columns).
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    assert_row_set(
        cur.fetchall(),
        tuple(row for row in LOANS if row[3] == "January 2026"),
        "Expected the loans whose loan_period is January 2026",
    )


def test_15_distinct_cities(connection):
    """
    Query 6

    Show distinct cities.
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    rows = {
        row[0]
        for row in cur.fetchall()
    }

    assert rows == {
        "Casablanca",
        "Rabat",
        "Marrakech"
    }


def test_16_member_count(connection):
    """
    Query 7

    Count members.
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    result = cur.fetchone()[0]

    assert result == 3


def test_17_average_age(connection):
    """
    Query 8

    Find average age.
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    result = float(cur.fetchone()[0])

    assert round(result, 2) == 21.33


def test_18_names_starting_with_a(connection):
    """
    Query 9

    Find members whose first name starts with A (all columns).
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    assert_row_set(
        cur.fetchall(),
        tuple(row for row in MEMBERS if row[1].startswith("A")),
        "Expected members whose first name starts with A",
    )


def test_19_age_between_20_and_22(connection):
    """
    Query 10

    Find members aged between 20 and 22 inclusive (all columns).
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    assert_row_set(
        cur.fetchall(),
        tuple(row for row in MEMBERS if 20 <= row[3] <= 22),
        "Expected members whose age is between 20 and 22 inclusive",
    )


def test_20_sorted_members(connection):
    """
    Query 11

    List all members (all columns), sorted by city ascending,
    then age descending.
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    rows = cur.fetchall()
    expected = tuple(
        sorted(MEMBERS, key=lambda row: (row[4], -row[3]))
    )
    assert rows == expected, (
        "Rows should be sorted by city ascending, then age descending"
    )


def test_21_first_two_members(connection):
    """
    Query 12

    Retrieve the first two members when sorted by member_id
    (all columns).
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    rows = cur.fetchall()
    expected = tuple(sorted(MEMBERS, key=lambda row: row[0])[:2])
    assert rows == expected, "Expected the two members with the smallest member_id, in that order"


def test_22_loans_grouped_by_period(connection):
    """
    Query 13

    Count loans per loan period using GROUP BY.
    Return two columns: loan_period and the number of loans.
    """

    cur = connection.cursor()

    cur.execute("USE LibraryDB")

    sql = """
    -- WRITE YOUR SQL HERE
    """

    execute_sql(cur, sql)

    rows = cur.fetchall()
    assert rows, "Expected one row per loan period"
    assert len(rows[0]) >= 2, "Return two columns: loan_period and the number of loans"
    counts = {row[0]: int(row[1]) for row in rows}

    assert counts == {
        "January 2026": 2,
        "February 2026": 1,
    }
