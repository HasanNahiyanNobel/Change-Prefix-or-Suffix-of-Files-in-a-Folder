#
# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
#
import ntpath
import os

path = os.getcwd() + "\Sample Directory 1"
# path = "G:\Varsity (Academic Stuffs)\Recordings of 4-1 (January, 2021)\CSE 311 Recordings"

for file_path in os.scandir(path):
	file_name = ntpath.basename(file_path)

	only_directory = ntpath.dirname(file_path)
	only_file_name = file_name.split(".")[0]
	only_extension = file_name.split(".")[1]

	only_file_name = "CSE 311 " + only_file_name
	# only_file_name = only_file_name[8:]

	new_file_path = only_directory + "\\" + only_file_name + "." + only_extension

	os.rename(file_path.path, new_file_path)
