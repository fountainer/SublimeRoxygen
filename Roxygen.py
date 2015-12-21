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

        snippet = "#' Title\n#'\n#' <full description>\n"

        for p in params:
            snippet += "#' @param %s \n" % p

        snippet += "#' @return\n#' \n#' @export\n#' \n#' @examples"

        self.view.insert(edit, sel.begin(), snippet)
