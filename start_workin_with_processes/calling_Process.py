import os
import sys

program = "python"
print("Process is Calling")
argguments = ["called_Process.py"]

# we call the called_Process.py script
os.execvp(program, (program,) + tuple(argguments))  # starts a new process, replacing the current one!
print("Good Bye!")