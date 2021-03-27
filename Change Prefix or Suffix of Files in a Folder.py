#
# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
#
import ntpath
import os

path = os.getcwd() + "\Sample Directory 1"
# path = "G:\Varsity (Academic Stuffs)\Recordings of 4-1 (January, 2021)\CSE 311 Recordings"

prefix_to_add = ""
prefix_to_rmv = "Copy of "
suffix_to_add = ""
suffix_to_rmv = " Haha"

for file_path in os.scandir(path):
	file_name = ntpath.basename(file_path)

	only_directory = ntpath.dirname(file_path)
	only_file_name = file_name.split(".")[0]
	only_extension = file_name.split(".")[1]

	# Remove matched prefix
	if only_file_name[:len(prefix_to_rmv)] == prefix_to_rmv:
		only_file_name = only_file_name[len(prefix_to_rmv):]

	# Remove matched suffix
	if only_file_name[-len(suffix_to_rmv):] == suffix_to_rmv:
		only_file_name = only_file_name[:-len(suffix_to_rmv)]

	# Add desired prefix and suffix
	only_file_name = prefix_to_add + only_file_name + suffix_to_add

	# Create the new file path
	new_file_path = only_directory + "\\" + only_file_name + "." + only_extension

	# Rename that path
	os.rename(file_path.path, new_file_path)