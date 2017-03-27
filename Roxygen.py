import sublime
import sublime_plugin
import os
import subprocess
import string


class RoxygenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()[0]
        params_reg = self.view.find('(?<=\()(.|\n)*?(?=\))', sel.begin())
        params_txt = self.view.substr(params_reg)
        params = extract_param(params_txt)

        snippet = "#' Title\n#'\n"

        for p in params:
            snippet += "#' @param %s \n" % p

        snippet += "#'\n#' @return \n#' \n#' @export\n#' \n#' @examples\n#' "

        self.view.insert(edit, sel.begin(), snippet)

class RcommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()[0]
        params_reg = self.view.find('(?<=\()(.|\n)*?(?=\))', sel.begin())
        params_txt = self.view.substr(params_reg)
        params = extract_param(params_txt)
        snippet = "# \n"
        for p in params:
            snippet += "# @param %s \n" % p

        snippet += "# @return "
        self.view.insert(edit, sel.begin(), snippet)

def extract_param(text):
    params = text.split(',')
    params = [p.strip("\n") for p in params]
    params = [p.split("=")[0] for p in params]
    params = [s.strip() for s in params]
    length_max = max([len(str) for str in params])
    params = [p + " " * (length_max - len(p)) for p in params]
    return(params)

class RcppCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()[0]
        params_reg = self.view.find('(?<=\()(.|\n)*?(?=\))', sel.begin())
        params_txt = self.view.substr(params_reg)
        params = extract_param(params_txt)
        params = [p.split()[1] for p in params]
        length_max = max([len(str) for str in params])
        params = [p + " " * (length_max - len(p)) for p in params]
        snippet = "//' Title\n//'\n"

        for p in params:
            snippet += "//' @param %s \n" % p

        snippet += "//'\n//' @return \n//' \n//' @export\n//' \n//' @examples\n//' \n// [[Rcpp::export]]"
        self.view.insert(edit, sel.begin(), snippet)
