#!/usr/bin/env python3

# Author: Raymond Malicdem
# Date Created: 4-Sep-2021 
# Description: Terminal based python script program that prints text
#				when run either as a program or imported as a module

import hellotext


def main():
	print("in main module")
	print(hellotext.helloworld_pythonic_func())
	print(hellotext.helloworld_derived_cfunc("hello", "world"))


if __name__ == "__main__":
	main()