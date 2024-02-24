# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
#!/usr/bin/python

from pathlib import Path

lab_path = "/home/gary/workspace/codingnomads/python-101-main"
p_lab_path = Path(lab_path)

#type(p_lab_path)
#print(p_lab_path)

print(f"{'FILENAME': <35} {'FILEDIRECTORY'}")

for pyfile in p_lab_path.rglob('*.py'):
   print(f"{pyfile.name: <35} {pyfile.parent}")
  
   #print(f"{'Filename:'}{pyfile.name: <35} {'Filedir:'}{pyfile.parent}")

    

    