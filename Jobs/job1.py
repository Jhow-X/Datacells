import os
from os.path import exists
import pandas as pd

if not (exists("../Datasets/covid.csv")):
    os.system("curl -o covid.csv https://raw.githubusercontent.com/Jhow-X/Coisas-da-facul/master/covid.csv")
    os.system("mv covid.csv ../Datasets/covid.csv")
else:
    actual = pd.read_csv("../Datasets/covid.csv")
    new = pd.read_csv("https://raw.githubusercontent.com/Jhow-X/Coisas-da-facul/master/covid.csv")
    if(len(new)> len(actual)):
        os.system("curl -o covid.csv https://raw.githubusercontent.com/Jhow-X/Coisas-da-facul/master/covid.csv")
        os.system("mv covid.csv ../Datasets/covid.csv")
        os.system("python3 job2.py")
 