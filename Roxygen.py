import sublime
import sublime_plugin
import os
import subprocess
import string


class RoxygenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()[0]

        params_reg = self.view.find('(?<=\().*(?=\))', sel.begin())
        params_txt = self.view.substr(params_reg)
        params = params_txt.split(',')
        params = [p.split("=")[0] for p in params]
        params = [s.strip() for s in params]
        length_max = max([len(str) for str in params])
        params = [p + " " * (length_max - len(p)) for p in params]

        snippet = "#' Title\n#'\n#' <full description>\n"

        for p in params:
            snippet += "#' @param %s \n" % p

        snippet += "#' @return\n#' \n#' @export\n#' \n#' @examples"

        self.view.insert(edit, sel.begin(), snippet)

class RcommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()[0]
        params_reg = self.view.find('(?<=\().*(?=\))', sel.begin())
        params_txt = self.view.substr(params_reg)
        params = params_txt.split(',')
        params = [p.split("=")[0] for p in params]
        params = [s.strip() for s in params]
        length_max = max([len(str) for str in params])
        params = [p + " " * (length_max - len(p)) for p in params]
        snippet = "# \n"
        for p in params:
            snippet += "# @param %s \n" % p

        snippet += "# @return"
        self.view.insert(edit, sel.begin(), snippet)