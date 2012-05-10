#!/usr/bin/python
#########################################################
# Application Birazer									#
# =========== =======									#
# Search empty folders with a specified					#
# directory, it can erase it too. 						#
#														#
# C0d3r: Julian Alexader Murillo (Lexinerus)			#
# 05-Abr-2012											#
#########################################################
import os
import sys
import properties
from messages import *

list_path_to_delete = []
message = Messages()

def fix_dir_path(directory):
	last_i = len(directory) - 1
	is_last_slash = directory[last_i] == properties.SLASH
	directory = directory[:last_i] if is_last_slash else directory
	return directory

# Method to show all empty directories
# inside a specified directory.
def show_empty_folders(directory, recursive):
	directory = fix_dir_path(directory)
	if not os.path.exists(directory):
		return	

	list_dir = os.listdir(directory)

	# Cicle that go through all directorys
	for file_name in list_dir:
		if file_name[:1] == properties.DOT:
			continue
	
		file_path = properties.PATH_CONV % (directory, file_name)
		if os.path.isdir(file_path):
			found_directories(file_path, recursive)			

# Method that found the empty directories
def found_directories(file_path, recursive):
	try:
		# Test if the directory has something
		os.listdir(file_path)[0]
		if recursive:
			show_empty_folders(file_path, recursive)
	except:
		# If the directory has nothing so is empty
		message_text = properties.EMPTY_MESSAGE % file_path
		message.show_message(1, message_text)
		list_path_to_delete.append(file_path)

def masive_delete_folders(folders):
	for folder in folders:
		command = properties.RM_COMMAND % folder
		os.system(command)
		message.show_message(0, properties.DIR_DELETED % folder)

# Shows messages to deside if going to delete empty folders
# or not.
def delete_ui(list_path_to_delete):
	yes = properties.Y
	delete = None
	for_dummies = None
	if not list_path_to_delete:
		message.show_message(5, properties.NO_DIRS)
	else:
		delete_message = properties.Q_DEL_EMPTY
		delete = raw_input(delete_message)
	
	if delete == yes:
		delete_message = properties.Q_SURE
		for_dummies = raw_input(delete_message)

	if for_dummies == yes:
		masive_delete_folders(list_path_to_delete)
		print properties.DELETED

def show_help():
	message.show_message(0, properties.HELP_MESSAGE)
	message.show_message(0, properties.RECURSIVE_MESSAGE)

# Main thread
def main():
	print properties.TITLE
	recursive = False
	directory = sys.argv[1]

	if sys.argv[1] == properties.H or sys.argv[1] == properties.HELP:
		show_help()
		return

	if sys.argv[1] == properties.R or sys.argv[1] == properties.RECURSIVE:
		recursive = True
		directory = sys.argv[2]

	if not os.path.exists(directory):
		message.show_message(0, properties.NOT_EXIST % directory)
		return	

	message_text = properties.SCANNING % directory	
	message.show_message(2, message_text)

	# Shows the empty folders and store it on an array 
	# to be deleted later
	show_empty_folders(directory, recursive)
	delete_ui(list_path_to_delete)
	

if __name__ == "__main__":
	main()
