#! /usr/bin/python

import os, argparse, sys
from engine.router import Router

scriptPath = os.path.dirname(os.path.realpath(__file__))

version = "0.1"
releaseDate = "2012-03-14"
description = "Blast for Basis! v%s" % version
license = open(scriptPath + "/LICENSE")

#
# Get the command from the command line. Determine
# if the command actually exists. If not let the
# user know.
#
parser = argparse.ArgumentParser(description = description)

parser.add_argument("command", help = "Name of the Blast command to execute", nargs = '*')
args = parser.parse_args()


print ""
print description
print license.read()
print ""

router = Router(args, scriptPath)
if not router.validate():
	print "'%s' is not a valid command" % args.command
	sys.exit()

print "Command: %s" % args.command[0]
router.run()
