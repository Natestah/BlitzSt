import sublime_plugin
import sublime
import sublime_api
import json
import os

from .BlitzIPC import ipc

class BlitzEventListener(sublime_plugin.EventListener):

	def __init__(self):
		print("started BlitzEventListener")

	def on_deactivated(self, view):
		print("on_deactivated")

	def on_activated(self, view):
		print("on_activated")
		
	def plugin_loaded(self):
		print("blitz plugin_loaded")

	def on_new_project(self, window):
		self.update_blitz_workspaces()

	def on_load_project(self, window):
		self.update_blitz_workspaces()

	def on_new_window(self, window):
		self.update_blitz_workspaces()

	def update_blitz_workspaces(self):
		list_of_workspaces = []
		for index, value in enumerate(sublime.windows()):
			if(value):
				list_of_paths = [];
				list_of_names = [];
				folders = value.folders()

				project_name = value.project_file_name()
				if(project_name):
					print("Project Name: " + project_name)
				workspace_file_name = value.workspace_file_name()
				if(workspace_file_name):
					print("Workspace FileName: " + workspace_file_name)


				projectdata = value.project_data()
				if projectdata:
					for folder in projectdata["folders"]:

						if not os.path.exists(folder["path"]) and workspace_file_name:

							relative_to = os.path.dirname(workspace_file_name)
							test_relative = os.path.join(relative_to,folder["path"])
							if(os.path.exists(test_relative)):
								list_of_paths.append(test_relative)
						else:
							list_of_paths.append(folder["path"])
						if "name" in folder:
	 						list_of_names.append(folder["name"])
						else:
	 						list_of_names.append(folder["path"])
				else:
					for folder in value.folders():
						if folder:
							list_of_paths.append(folder)
							list_of_names.append(folder)
				data = {
				"ExeForIcon":"subl.exe",
				"Folders":list_of_paths,
				"FolderNames":list_of_names,
				"ProjectName":project_name,
				"WorkspaceFileName":workspace_file_name
				}
				if len(list_of_paths) > 0:
					list_of_workspaces.append(data)
		ipc.sendCommand("SUBLIME_TEXT_WORKSPACE", json.dumps(list_of_workspaces,indent=4));

	def on_init(self,views):
		self.update_blitz_workspaces()
		

