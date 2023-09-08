# process.py

# Import necessary libraries for file operations
import os

# Modify a file in the repository
file_path = "./file.txt"
with open(file_path, "a") as file:
    file.write("This is a new line added by process.py\n")

# Commit changes using Git within the GitHub Action
os.system("git config --global user.email 'kogcyc@gmail.com'")
os.system("git config --global user.name 'Matthew Grimm'")
os.system("git add .")
os.system("git commit -m 'Modify file using GitHub Action'")
os.system("git push origin main")
