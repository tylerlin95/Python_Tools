# =====================================
# FileName: file.py
# Usage: $python3 file.py arg1…
# Description: ...
# Dependency: numpy, PyTorch...
# Author: Lynn <lynn840429@gmail.com>
# Version: v1.1.0: 大版更新版本號.小更新版本號.bug修正版本號, Date
# =====================================
""" Import Package """
import os
import sys
import argparse
import numpy as np
import pandas as pd



""" User Defined Parameter """
PARAMETER_1 = 1



""" Folder/Path/Parameter Setting """
FOLDER_1 = "./"
PATH_1 = "./"
GLONAL_CONSTANT_NAME = 1



""" Class """
class ClassName(object):
	"""
	Class Info: ...
		Parameters:
		- 
		Returns:
		- 
	"""
	def __init__(self, ):
		pass
	
	def function_name(self, ):
		"""
		Function Info: ...
			Parameters:
				- 
			Returns:
				-
		"""
		pass



""" Function """
def function_name():
	"""
	Function Info: ...
		Parameters:
		- 
		Returns:
		- 
	"""
	var_name = 1


def parse_args():
	"""
	Function Info: Read in arguments from the command.
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--in_file", type=str, default="../requirement.txt", help="Input File Path/Name, ex: ../requirement.txt")
	
	return parser.parse_args()


def read_file(file_name=''):
	"""
	Function Info: Read the content fo the file and store it into [List]content.
	"""
	try:
		with open(file_name, 'r') as fn:
			content = fn.read().splitlines()
	except IOError:
		print("Error happened when reading %s" %(file_name))
		sys.exit()
	else:
		return content



""" Main """
def main():
	"""
	Function Info: Main Program
	"""
	args = parse_args()
	print("File Name:", args.in_file)
	print("Content:", read_file(args.in_file))



""" Boilerplate Code"""
if __name__ == '__main__':
	main()
	