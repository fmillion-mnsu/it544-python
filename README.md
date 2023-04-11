# Accessing Oracle Database and Microsoft SQL Server from Python

This code will show you how you can access both Oracle Database and MS SQL from Python. It will demonstrate running a few queries as well as interacting with both databases simultaneously.

The basic version of the code in this repository works directly with the database servers and requires you to write queries, as you'll see in the code. An alternative option which is commonly used in modern programming environments is to use an object-relational mapper (ORM), which lets you represent the data tables as Python class instances (or whatever language you are working with). This is an advanced topic that we may explore later.

## Setting up the project

The main thing you need on your system is [Python](https://www.python.org/downloads/) (obviously!). Along with that, it's strongly recommended that you use an IDE such as PyCharm or VS Code to work with the code. 

You also need to have `pip` installed, which is Python's built in package management toolset. On Windows, once you have Python installed, you should be able to run these commands at a command prompt to make sure `pip` is installed and updated to the latest version:

    python -m ensurepip
    python -m pip install -U pip

Finally, you need the `virtualenv` module, which lets you setup virtual environments. Alternatively, `anaconda` has a similar capability with the `conda` package manager. These instructions will use `virtualenv`, but if you're using `anaconda`, I can provide separate support for that. 

To install `virtualenv`:

    python -m pip install virtualenv

Next, [**download the repository**](https://github.com/fmillion-mnsu/it544-python/archive/refs/heads/master.zip) to your computer, and extract it to a path somewhere on your system.

Then, open a **command prompt** and use the `cd` command to move to the path you extracted the files to.

Finally, **run these commands** to setup the virtual environment and download the required Python packages:

    python3 -m virtualenv venv
    venv\scripts\activate.bat
    pip install -r requirements.txt

> If you are on Linux, it's likely you already have a Python installed on your system. These instructions will be mostly the same, except you will use the command `source venv/bin/activate` instead of `venv\scripts\activate.bat`.

### Oracle Instant Client

Since our servers are running Oracle 11g, you need to use [Oracle Instant Client](https://download.oracle.com/otn_software/nt/instantclient/1918000/instantclient-basiclite-windows.x64-19.18.0.0.0dbru.zip) to connect to the servers. 

Download the above link and open the ZIP file. You will see one folder named `instantclient_19_18` inside the ZIP file. **Extract this folder to the place where you extracted the source code.** Do not copy the files out of the folder - leave the folder intact!

You are now ready to run the code.

## Explaining the code

The code is contained in `program.py`.

The first part of the code contains configuration values that **you must set prior to running the code.** If you don't set these values, the code won't run - that's on purpose!

After you have set up the variables, you should be able to run the code. The variables default to the SP database, but you can (and should) change them as required by your assignments and projects.

You can see that it is quite straightforward to execute a `SELECT` query and iterate over the results. You can provide *any* `SELECT` query and iterate over it this way.

### Note about SQL Injection

When you are forming SQL queries, make sure to be mindful of SQL injection attacks - these are extremely easy to allow if you are simply concatenating strings together to form SQL statements. Something like `"SELECT * FROM myTable WHERE id = " + id` can prove *catastrophic* - the user could simply make `id` equal to a string such as `0; DROP TABLE myTable; --`. The resulting query would look like this: `SELECT * FROM myTable WHERE id = 0; DROP TABLE myTable;`!! 

To avoid SQL injection vulnerabilities, the easiest way is to use *parameterized* queries. You do this by replacing parts of the query that you expect to receive input from some other source (such as a user, a file, etc.) with an identifier in the query string - such as `%s`, `?` or `:` depending on the DBMS. For SQL Server, you can use `%s`, and for Oracle you can use `:` followed by an identifier.

> **Example safe query in Oracle:**
>
>     cursor.execute("select * from myTable where id = :id",(0,))
>
> **Example safe query in SQL Server:**
>
>     cursor.execute("select * from myTable where id = %s",(0,))

## For More Information

- [Developing Python Applications for Oracle Database](https://www.oracle.com/database/technologies/appdev/python/quickstartpythononprem.html) at Oracle.
- The [Python oracledb](https://python-oracledb.readthedocs.io/en/latest/index.html) documentation.
- The [Python pymssql](http://www.pymssql.org/en/stable/index.html) documentation.

