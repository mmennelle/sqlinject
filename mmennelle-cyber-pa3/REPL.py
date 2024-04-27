#!/usr/bin/env python

# REPL Example

import sys
import os


def interactiveShell():
    while True:
        inStr = input('lab3> ')
        if inStr == "exit":
            print('Good Bye')
            break
        else:
            print('do Stuff Here')
            os.system(inStr)
    return



if __name__ == "__main__":
	n = len(sys.argv)
	if n != 2:
		print('Enter Server IP address')
		print("Total arguments passed:", n)		
	else: 
		#sys.argv[0] is the name of the script
		#sys.argv[1] is arguments
		args = sys.argv[1:]
		siteIP = args[0]
		interactiveShell()