import os, sys, re
import shutil
import subprocess

class RunApp:
	__args = {}
	__cwd = ""
	__scriptPath = ""
	__os = "posix"

	__httpPort = "0"
	__docBase = ""

	def __init__(self, args, scriptPath):
		self.__args = args.command
		self.__cwd = os.getcwd()
		self.__scriptPath = scriptPath

		self.__httpPort = "8080"
		self.__docBase = self.__cwd.replace("\\", "/")

		self.__os = os.name


	def validate(self):
		return True


	def run(self):
		print "Running application on localhost:%s" % self.__httpPort

		exeName = "catalina.bat" if self.__os == "nt" else "catalina.sh"
		shell = True if self.__os == "nt" else False

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
		if os.getenv("JAVA_HOME") == None:
			raise Exception("Please set your JAVA_HOME environment variable")

		environment = {
			"CATALINA_HOME": self.__scriptPath + "/engine/tomcat",
			"JAVA_HOME": os.getenv("JAVA_HOME")
		}

		if self.__os == "nt":
			environment["SystemRoot"] = os.getenv("SystemRoot")

		subprocess.call([ "%s/engine/tomcat/bin/%s" % (self.__scriptPath, exeName), "run" ], shell = shell, env = environment)
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
