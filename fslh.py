import sublime
import sublime_plugin
import math

class FontSizeLineHeightCommand(sublime_plugin.TextCommand):
	def run(self, view):
		for region in self.view.sel():
			selection = self.view.substr(region).split(',')
			fontem = (int(selection[1]) / int(selection[0]))
			lineem = (int(selection[2]) / int(selection[1]))
			output = 'font-size: ' + str(fontem) + 'em;\nline-height: ' + str(lineem) + 'em;'
			self.view.replace(view, region, output)