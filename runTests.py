import sys
import os
import subprocess

output = open("result", "w")

for file in sorted(os.listdir(".")):
    if "teste" in file:
        print("running test: " + file)
        os.system("python T1Tree.py " + file)
