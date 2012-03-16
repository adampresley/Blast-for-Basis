import os, sys, re
import shutil

class CreateView:
	__args = {}
	__cwd = ""
	__scriptPath = ""

	def __init__(self, args, scriptPath):
		self.__args = args.command
		self.__cwd = os.getcwd()
		self.__scriptPath = scriptPath


	def validate(self):
		if len(self.__args) <= 1 or len(self.__args[1].split(".")) < 2:
			print "You must provide an action for your new view (command: 'create-view') in the form of SECTION.ACTION"
			return False

		return True


	def run(self):
		print "Creating new view for action '%s'" % self.__args[1]

		actionParts = self.__args[1].split(".")
		newViewPath = self.__cwd + "/views/" + actionParts[0]
		newViewFile = newViewPath + "/" + actionParts[1] + ".cfm"

		if not os.path.exists(newViewPath):
			os.makedirs(newViewPath)

		src = self.__scriptPath + "/engine/templates/newView.cfm"
		target = newViewFile
		shutil.copyfile(src, target)

		#
		# Fix the new file
		#
		fp = open(newViewFile, "rU")
		raw = fp.read()
		fp.close()

		raw = self.__fixFile(raw)

		fp = open(newViewFile, "w")
		fp.write(raw)
		fp.close()

		print "Done"
		

	def __fixFile(self, contents):
		fixes = [
			{ "pattern": re.compile('\$\{action\}', re.I | re.M), "replacement": self.__args[1] }
		]

		result = contents

		for p in fixes:
			result = p["pattern"].sub(p["replacement"], result)

		return result
