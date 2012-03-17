import os, sys, re
import shutil

class CreateDAO:
	__args = {}
	__cwd = ""
	__scriptPath = ""

	def __init__(self, args, scriptPath):
		self.__args = args.command
		self.__cwd = os.getcwd()
		self.__scriptPath = scriptPath


	def validate(self):
		if len(self.__args) <= 1:
			print "You must provide a name for your new DAO (command: 'create-dao')"
			return False

		return True


	def run(self):
		print "Creating new DAO '%s'" % self.__args[1]

		targetPath = self.__cwd + "/model/" + self.__args[1]

		src = self.__scriptPath + "/engine/templates/newDAO.cfc"
		target = targetPath + "/" + self.__args[1] + "DAO.cfc"

		if not os.path.exists(targetPath):
			os.makedirs(targetPath)

		#
		# Make a copy of the controller.cfc template
		#
		shutil.copyfile(src, target)

		#
		# Fix the new file
		#
		fp = open(target, "rU")
		raw = fp.read()
		fp.close()

		raw = self.__fixFile(raw)

		fp = open(target, "w")
		fp.write(raw)
		fp.close()

		print "Done"


	def __fixFile(self, contents):
		fixes = [
			{ "pattern": re.compile('\$\{daoName\}', re.I | re.M), "replacement": self.__args[1] }
		]

		result = contents

		for p in fixes:
			result = p["pattern"].sub(p["replacement"], result)

		return result
