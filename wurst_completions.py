
import sublime, sublime_plugin
import re


from common_j_natives     import common_j_natives
from common_j_constants   import common_j_constants
from blizzard_j_functions import blizzard_j_functions
from blizzard_j_constants import blizzard_j_constants
from wurst_stl_functions  import wurst_stl_funcs


PAIRINGS = common_j_natives + common_j_constants + blizzard_j_functions + blizzard_j_constants + wurst_stl_funcs
SUBLIME_FLAGS = sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS


class TagCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.wurst"):
            return []

        return (PAIRINGS, SUBLIME_FLAGS)
