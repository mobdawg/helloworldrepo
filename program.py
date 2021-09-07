#!/usr/bin/env python3

# Author: Raymond Malicdem
# Date Created: 4-Sep-2021 
# Description: Terminal based python script program that prints text
#				when run either as a program or imported a as module


import hello_text


if __name__ == "__main__":
	print("in main module")
else:
	print("from imported module")