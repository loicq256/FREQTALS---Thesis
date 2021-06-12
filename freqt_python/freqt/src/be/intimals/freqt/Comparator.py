#!/usr/bin/env python3

import sys

def comparator(args):
    javaFile = args[1]
    pythonFile = args[2]
    with open(javaFile) as jf:
        with open(pythonFile) as pf:
            jline = jf.readline()
            pline = pf.readline()
            while jline:
                if pline == "":
                    value = "python file is finish while java's file is not \n" + "Java line reach at the end of the python file: " + str(jline) + "\n"
                    return value
                if jline.strip() != pline.strip():
                    value = "File are different: \n" + "java: " + str(jline) + "\n" + "python: " + str(pline) + "\n"
                    return value
                jline = jf.readline()
                pline = pf.readline()
            if pline != "":
                value = "python file is longer than java file"
                return value
            else:
                value = "The files are identical"
                return value


if __name__ == '__main__':
    args = sys.argv[1:]
    value = comparator(args)
    print(value)
