# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots


import pathlib
from datetime import datetime

home = pathlib.Path.home()
now = datetime.now()
fnow = now.strftime('%Y%m%d-%H%M%S')
counter = 0    
       
working_path = pathlib.Path(input("What directory do you want to rename files?: "))
fex = input("What is the file extension of the files you want to rename? ex. .jpg: ")     
filename_base = f"{working_path}/Screenshot"


for filepath in working_path.iterdir():
    if filepath.is_file():
        if filepath.suffix == fex:
            counter += 1
            #print(f"{filename_base}{fnow}{counter}{fex}")
            filepath.rename(f'{filename_base}-{counter}{fex}')