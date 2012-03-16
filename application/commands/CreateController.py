import os, sys, re
import shutil

class CreateController:
	__args = {}
	__cwd = ""
	__scriptPath = ""

	def __init__(self, args, scriptPath):
		self.__args = args.command
		self.__cwd = os.getcwd()
		self.__scriptPath = scriptPath


	def validate(self):
		if len(self.__args) <= 1:
			print "You must provide a name for your new controller (command: 'create-controller')"
			return False

		return True


	def run(self):
		print "Creating new controller '%s'" % self.__args[1]

		src = self.__scriptPath + "/engine/templates/controller.cfc"
		target = self.__cwd + "/controllers/" + self.__args[1] + ".cfc"

		#
		# Make a copy of the controller.cfc template
		#
		shutil.copyfile(src, target)
		print "Done"
