# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there
#!/usr/bin/python

import pathlib

path = pathlib.Path.cwd()
home = pathlib.Path.home()
working_current = pathlib.Path(f"{home}/Pictures/Screenshots/")
working_new = pathlib.Path(f"{home}/Pictures/Screenshots/new_dir")

# create new dir, if it already exists dont error out just contiunu with out re-creating.
working_new.mkdir(exist_ok=True)

for filepath in working_current.iterdir():
    if filepath.is_file():
        if filepath.suffix == ".png":
            print(filepath.name)
            join_working_new = working_new.joinpath(filepath.name)
            filepath.replace(join_working_new)