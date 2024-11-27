import os
import sublime
import sublime_plugin
import subprocess
from .BlitzIPC import ipc


class BlitzSearchThis(sublime_plugin.TextCommand):
	def __init__(self, view):
		self.view = view
		self.for_replace = False

	def run(self, edit):
		view = self.view
		sel = view.sel()
		region1 = sel[0]
		wholeWord = 0
		if not ipc.blitzInstalled():
			ipc.gotoBlitzHomePage();
			return;
		if len(region1) == 0:
			wholeWord = 1
			view.run_command('find_under_expand')
		sel = view.sel()
		region1 = sel[0]
		if len(region1) == 0:
			print('no selection')
		searchText = ""
		searchText = view.substr(region1)
		if wholeWord == 1:
			searchText = '@' + searchText
		if self.for_replace:
			ipc.bootCommand("SET_REPLACE", searchText);
		else:
			ipc.bootCommand("SET_SEARCH", searchText);

	def is_enabled(self):
		if self.view is None:
			return False
		return True

