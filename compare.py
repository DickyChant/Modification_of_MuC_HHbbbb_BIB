import difflib
import sys
import os
from sys import argv

def read_file(filename):
    try:
        with open(filename,"r") as f:
            return f.readlines()
    except IOError:
        print(f"Error: File {filename} not found")
        sys.exit(1)

def compare_file(file1,file2,outfile = "diff.html"):
    f1_lines = read_file(file1)
    f2_lines = read_file(file2)

    d = difflib.HtmlDiff()
    res = d.make_file(f1_lines,f2_lines)
    with open(outfile,"w") as f:
        f.writelines(res)


if __name__ == "__main__":
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    print(f1,f2)
    compare_file(f1,f2)