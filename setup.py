#! /usr/bin/python

import os
from setuptools import setup

def read(filename):
	return open(os.path.join(os.path.dirname(__file__), filename)).read()


#
# Begin the program yo
#
setup(
	name = "Blast for Basis",
	version = "0.0.1",
	author = "Adam Presley",
	author_email = "adam@adampresley.com",
	description = "A set of tools for building CFML applications using the Basis framework.",

	license = "BSD",
	keywords = "CFML tools framework",
	url = "https://github.com/adampresley/Blast-for-Basis",
	packages = [ "blast", "blast.commands", "blast.engine", "blast.engine.templates", "blast.engine.tomcat", "blast.skeleton" ],
	include_package_data = True,
	package_data = {
		"": [ "*.*", "LICENSE", "NOTICE", "RELEASE-NOTES" ],
		"blast.engine": [ 
			"tomcat/bin/*.*", "tomcat/conf/*.*", "tomcat/lib/*.*", "tomcat/logs/*.*", "tomcat/temp/", "tomcat/webapps/", "tomcat/work/",
			"templates/*.*"
		],
		"blast.skeleton": [
			"cf-engine/WEB-INF/", "cf-engine/WEB-INF/bin/", "cf-engine/WEB-INF/bin/x64/", "cf-engine/WEB-INF/bluedragon/",
			"cf-engine/WEB-INF/classes/com/newatlanta/", "cf-engine/WEB-INF/customtags/", "cf-engine/WEB-INF/lib/",
			"cf-engine/WEB-INF/webresources/flowplayer/", "cf-engine/WEB-INF/webresources/js/", "cf-engine/bluedragon/adminapi/",
			"cf-engine/bluedragon/adminapi/docs/", "cf-engine/bluedragon/adminapi/utils/"
		]
	},
	long_description = read("README.md"),
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Topic :: Utilities",
		"License :: BSD License"
	]
)