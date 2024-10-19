import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

def autofill(char="", attri=""):
    if char == "" and attri =="": char = input("What character? "); attri = input("What attribute? "); return char, attri
    elif char == "" and attri !="": char = input("What charater? "); return char, attri
    elif char !="" and attri =="": attri = input("What attribute? "); return char, attri
    else: return char, attri