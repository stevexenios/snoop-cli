# SNOOP CLI

## Summary

Snoop is a cli developed using the Python package Click.

## Setup

To use it, cd into ```snoop``` directory and run:

1. ```virtualenv venv``` after opening terminal in the **```snoop```** directory.
2. ```. venv/bin/activate``` or ```. venv/Scripts/activate``` depending on your venv.
3. ```pip install --upgrade pip```
4. ```pip install pandas```
5. ```pip install --editable .```



## Repo Structure

```
snoop-cli
├── in
    └── reviews.csv
├── out
    ├── sitters.csv
    └── sitters.txt
├── snoop
    ├──compute.py
    ├──setup.py
    ├──snoop.py
    └──test.py
└── README.md
 
1 repo, 3 sub-directories, 7 files
```

## Description

### 1. ```in```

Contains the input ```.csv``` file.

### 2. ```out```

Contains the resulting output ```.csv``` file.

### 3. ```snoop```

This is where the code resides for setting everything up.

This is the cli package. **snoop** is the name of the application, and also main command.

**a. ```compute.py```**: contains the code to do the search ranking of the sitters.

**b. ```setup.py```**: code for setting everything up.

**c. ```snoop.py```**: this module has the the implementations of our commands.


## Sample commands to run

```snoop_cli
1. snoop --compute --i ../in/reviews.csv --o ../out/sitters.csv bark --string Batman

2. snoop --s bark --string Batwoman --repeat 10

3. snoop --help
```

## Sources

###### 1. [click](https://click.palletsprojects.com/en/7.x/)
