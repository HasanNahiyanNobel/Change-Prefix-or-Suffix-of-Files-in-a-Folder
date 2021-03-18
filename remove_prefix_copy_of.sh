#!/bin/sh

# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
# This script removes the prefix "Copy of" from files of the current directory (not recursively)

number_of_files_renamed=0
word_to_remove_1="Copy"
word_to_remove_2="of"

for file_name in * ; do	
	
	IFS=' ' read -r -a array <<< "$file_name"
	
	if [ ${array[0]} = $word_to_remove_1 ] && [ ${array[1]} = $word_to_remove_2 ]; then
		
		file_name_without_copy="${file_name#* }"
		file_name_without_copy_of="${file_name_without_copy#* }"
		
		# echo "File name is: $file_name_without_copy_of"
		mv "$file_name" "$file_name_without_copy_of"
		
		number_of_files_renamed=`expr $number_of_files_renamed + 1`
	fi
done

echo "Removed prefix from $number_of_files_renamed files."
