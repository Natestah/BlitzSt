import sublime
import sublime_plugin
import subprocess
import os


envProgramFiles = os.environ.get('programfiles')
envProgramFilePath = os.path.join(envProgramFiles, 'Blitz','Blitz.exe');
appdata = os.environ.get("appdata")
ipcPath = os.path.join(appdata, 'NathanSilvers','POORMANS_IPC')

class BlitzIPC:

	def __init__(self):
		if not os.path.exists(ipcPath):
			os.makedirs(ipcPath)

	def getIPCPath(self):
		return ipcPath

	def blitzInstalled(self):
		return os.path.exists(envProgramFilePath)

	def gotoBlitzHomePage(self):
		os.startfile('https://natestah.com/download')

	def sendCommand(self, command, contents):
		ipcFile = os.path.join(ipcPath,command + ".txt" )
		f = open(ipcFile, "w")
		f.write(contents)
		f.close()

	def bootCommand(self, command, contents):
		self.sendCommand(command, contents)
		os.startfile(envProgramFilePath)

if 'ipc' not in globals():
	ipc = BlitzIPC()
