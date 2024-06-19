import os
import sublime
import sublime_plugin
import subprocess

class BlitzSearchThis(sublime_plugin.TextCommand):
	def __init__(self, view):
		self.view = view

	def run(self, edit):
		view = self.view
		sel = view.sel()

		region1 = sel[0]
		wholeWord = 0
		if len(region1) == 0:
			wholeWord = 1
			view.run_command('find_under_expand')
		sel = view.sel()
		region1 = sel[0]
		if len(region1) == 0:
			print('no selection')
			return;

		envProgramFiles = os.environ.get('programfiles')
		envProgramFilePath = os.path.join(envProgramFiles, 'Blitz','Blitz.exe');

		if not os.path.exists(envProgramFilePath):
			os.startfile('https://natestah.com')
			return;

		selectionText = view.substr(region1)
		if wholeWord == 1:
			selectionText = '@' + selectionText

		appdata = os.environ.get("appdata")
		ipcPath = os.path.join(appdata, 'NathanSilvers','POORMANS_IPC')

		if not os.path.exists(ipcPath):
			os.makedirs(ipcPath)
		ipcFile = os.path.join(ipcPath,'SET_SEARCH.txt' )

		f = open(ipcFile, "w")
		f.write(selectionText)
		f.close()

		os.startfile(envProgramFilePath)

	def is_enabled(self):
		if self.view is None:
			return False
		return True

