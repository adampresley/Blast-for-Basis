import json, os

class Router:
	__args = {}
	__mapping = {}
	__scriptPath = ""

	def __init__(self, args, scriptPath):
		self.__args = args
		self.__scriptPath = scriptPath
		self.__loadMapping()


	def validate(self):
		result = True
		if not self.__args.command or not self.__args.command[0] in self.__mapping:
			result = False

		return result


	def run(self):
		route = self.__mapping[self.__args.command[0]]
		className = route.split(".")[-1]

		module = __import__(route, fromlist = [ className ])
		class_ = getattr(module, className)
		instance = class_(self.__args, self.__scriptPath)

		#
		# First validate that the command has all it needs, then run
		#
		if instance.validate():
			instance.run()


	def __loadMapping(self):
		rawData = open(self.__scriptPath + "/engine/mapping.json", "r")
		self.__mapping = json.load(rawData)
