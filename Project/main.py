# Potential to comment out
import sys
import os

# Add the parent directory of "Python" to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# Potential to comment out above
from Python.Project.module1 import add
from Python.Project.module2 import subtract

print(add(5, 3))
print(subtract(5, 3))
