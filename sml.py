#!/usr/bin/python

import json, os, subprocess, sys, argparse

class SML:
	"""The SML class"""
	def __init__(self):
		f = open('sml.json')
		self.data = json.load(f)
		f.close()

	def listModules(self):
		for k in self.data.keys():
			print "%s:" % k,
			for ver in  self.data[k]:
				print "%s" % ver,
			print 

	def findModuleWithVersion(self, module, version):
		if (module in self.data) != True:
			sys.exit("Module %s not found!" % module)
			return

		if (version in self.data[module]) != True:
			sys.exit("Version %s of module %s not found!" % (version, module))
			return

		return self.data[module][version]

	def loadModule(self, module, version):
		info = self.findModuleWithVersion(module, version)

		ePATH = os.getenv('PATH', '')
		ePATH += ':' + info['base'] + info['bin']

		print "setvar PATH=" + ePATH

	def unloadModule(self, module, version):
		info = self.findModuleWithVersion(module, version)

		ePATH = os.getenv('PATH', '')
		remove = ':' + info['base'] + info['bin']
		ePATH = ePATH.replace(remove, '')

		print "setvar PATH=" + ePATH



sml = SML()
#SML.listModules()
#sml.loadModule("llvm", "svn-release");
#sml.unloadModule("llvm", "svn-release")

parser = argparse.ArgumentParser(prog='Prog')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--load', nargs=2, metavar=('module', 'version'), help='load a module')
group.add_argument('--unload', nargs=2, metavar=('module', 'version'), help='unload a module')
group.add_argument('--list', action='store_true', help='list all modules')

args = parser.parse_args()

#print args

if args.list:
	sml.listModules()
elif args.load:
	sml.loadModule(args.load[0], args.load[1])
elif args.unload:
	sml.unloadModule(args.unload[0], args.unload[1])
