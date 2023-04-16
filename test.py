import numpy as np

with open("Base/meshDict") as f:
    lines = f.readlines()
    if(lines=="###"):
        print(lines+"n")