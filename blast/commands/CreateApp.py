import os, sys, re
import distutils.dir_util

class CreateApp:
	__args = {}
	__path = ""
	__cwd = ""
	__scriptPath = ""

	def __init__(self, args, scriptPath):
		self.__args = args.command
		self.__cwd = os.getcwd()
		self.__scriptPath = scriptPath


	def validate(self):
		if len(self.__args) <= 1:
			print "You must provide a name for your new application (command: 'create-app')"
			return False

		self.__path = self.__cwd + "/" + self.__args[1]
		return True


	def run(self):
		print "New application name: %s\n" % self.__args[1]

		self.__createDirectory()
		self.__copyFiles()
		

		print "Your new application '%s' is ready. To begin change directory to %s and type 'blast run-app'." % (self.__args[1], self.__args[1])


	def __createDirectory(self):
		print "Digging up a directory..."

		if not os.path.exists(self.__path):
			os.makedirs(self.__path)


	def __copyFiles(self):
		print "Carefully placing files..."
		
		distutils.dir_util.copy_tree(self.__scriptPath + "/skeleton/framework", self.__path, preserve_symlinks = 1)
		self.__setupProject()

		distutils.dir_util.copy_tree(self.__scriptPath + "/skeleton/cf-engine", self.__path, preserve_symlinks = 1)


	def __setupProject(self):
		for root, subfolders, files in os.walk(self.__path):
			for file in files:
				fp = open(os.path.join(root, file), "rU")
				raw = fp.read()
				fp.close()

				raw = self.__fixFile(raw)

				fp = open(os.path.join(root, file), "w")
				fp.write(raw)
				fp.close()


	def __fixFile(self, contents):
		fixes = [
			{ "pattern": re.compile('\$\{appName\}', re.I | re.M), "replacement": self.__args[1] }
		]

		result = contents

		for p in fixes:
			result = p["pattern"].sub(p["replacement"], result)

		return result
