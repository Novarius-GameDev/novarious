#!/usr/bin/env python

import os
import sys
import subprocess

def intro():
	os.system("clear")
	print ""
	print " Welcome To..."
	print "   _   _  ______      __     _____  _____ _    _  _____ "
	print "  | \ | |/ __ \ \    / /\   |  __ \|_   _| |  | |/ ____|"
	print "  |  \| | |  | \ \  / /  \  | |__) | | | | |  | | (___  "
	print "  | . ` | |  | |\ \/ / /\ \ |  _  /  | | | |  | |\___ \ "
	print "  | |\  | |__| | \  / ____ \| | \ \ _| |_| |__| |____) |"
	print "  |_| \_|\____/   \/_/    \_\_|  \_\_____|\____/|_____/ "
	print ""

def startFiles():
	print " [*] Reading from file 'startup.lst'"
	try:
		startup = open("startup.lst", "r")
		for line in startup:
			line = line.strip("\n")
			print " [+] Starting program " + line.split("###", 1)[0]
			process = subprocess.Popen(line.split("###", 1)[1], shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
			output = process.stdout.read() + process.stderr.read()
			if len(output) > 0:
				print " [-] Error Loading File : " + line.split("###", 1)[1]
				startup.close()
				return None
			else:
				print " [+] File Loaded : " + line.split("###", 1)[1]
		print " [+] All Files Loaded"
		startup.close()
	except:
		print " [-] File Empty Or Not Found"

def main():
	intro()
	startFiles()
	print ""

main()
