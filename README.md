# Accessing Oracle Database and Microsoft SQL Server from Python

This code will show you how you can access both Oracle Database and MS SQL from Python. It will demonstrate running a few queries as well as interacting with both databases simultaneously.

The basic version of the code in this repository works directly with the database servers and requires you to write queries, as you'll see in the code. An alternative option which is commonly used in modern programming environments is to use an object-relational mapper (ORM), which lets you represent the data tables as Python class instances (or whatever language you are working with). This is an advanced topic that we may explore later.

## Setting up the project

The main thing you need on your system is [Python](https://www.python.org/downloads/) (obviously!). Along with that, it's strongly recommended that you use an IDE such as PyCharm or VS Code to work with the code. 

You also need to have `pip` installed, which is Python's built in package management toolset. On Windows, once you have Python installed, you should be able to run these commands at a command prompt to make sure `pip` is installed and updated to the latest version:

    python3 -m ensurepip
    python3 -m pip install -U pip

Finally, you need the `virtualenv` module, which lets you setup virtual environments. Alternatively, `anaconda` has a similar capability with the `conda` package manager. These instructions will use `virtualenv`, but if you're using `anaconda`, I can provide separate support for that. 

To install `virtualenv`:

    python3 -m pip install virtualenv

Next, [**download the repository**](https://github.com/fmillion-mnsu/it544-python/archive/refs/heads/master.zip) to your computer, and extract it to a path somewhere on your system.

Then, open a **command prompt** and use the `cd` command to move to the path you extracted the files to.

Finally, run these commands to setup the virtual environment and download the required Python packages:

    python3 -m virtualenv venv
    venv\scripts\activate.bat
    pip3 install -r requirements.txt

> If you are on Linux, it's likely you already have a Python installed on your system. These instructions will be mostly the same, except you will use the command `source venv/bin/activate` instead of `venv\scripts\activate.bat`.

You are now ready to run the code.

## Explaining the code

The code is contained in `program.py`.
