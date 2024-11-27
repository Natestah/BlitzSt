import os
import sublime
import sublime_plugin
import subprocess
from .BlitzSearchThis import BlitzSearchThis
from .BlitzIPC import ipc


class BlitzReplaceThis(sublime_plugin.TextCommand):

	def __init__(self, view):
		self.searchthis = BlitzSearchThis(view)
		self.searchthis.for_replace = True
		self.view = view

	def run(self, edit):
		self.searchthis.run(edit)

	def is_enabled(self):
		return self.searchthis.is_enabled()

