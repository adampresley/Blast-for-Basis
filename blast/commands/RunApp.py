import os, sys, re
import shutil
import subprocess

class RunApp:
	__args = {}
	__cwd = ""
	__scriptPath = ""

	__httpPort = "0"
	__docBase = ""

	def __init__(self, args, scriptPath):
		self.__args = args.command
		self.__cwd = os.getcwd()
		self.__scriptPath = scriptPath

		self.__httpPort = "8080"
		self.__docBase = self.__cwd


	def validate(self):
		return True


	def run(self):
		print "Running application on localhost:%s" % self.__httpPort

		src = self.__scriptPath + "/engine/templates/server.xml"
		target = self.__scriptPath + "/engine/tomcat/conf/server.xml"

		#
		# Make a copy of the server.xml template and replace some stuff
		#
		shutil.copyfile(src, target)

		fp = open(target, "rU")
		raw = fp.read()
		fp.close()

		raw = self.__fixFile(raw)

		fp = open(target, "w")
		fp.write(raw)
		fp.close()

		#
		# Start up Tomcat
		#
		subprocess.check_call([ "%s/engine/tomcat/bin/catalina.sh" % (self.__scriptPath), "run" ])
		sys.exit()


	def __fixFile(self, contents):
		fixes = [
			{ "pattern": re.compile('\$\{httpPort\}', re.I | re.M), "replacement": self.__httpPort },
			{ "pattern": re.compile('\$\{docBase\}', re.I | re.M), "replacement": self.__docBase }
		]

		result = contents

		for p in fixes:
			result = p["pattern"].sub(p["replacement"], result)

		return result
