#! /usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" Tiny SublimeText3 plugin to add these commands:

'disable_spellcheck'
  - It disables shellcheck
  - It is NOT binded to any key

'enable_english_spellcheck'
  - It enables shellcheck and sets the dictionary to English
  - It is binded to the key chain ["ctrl+k", "ctrl+e"]

'enable_french_spellcheck'
  - It enables shellcheck and sets the dictionary to French
  - It is binded to the key chain ["ctrl+k", "ctrl+f"]

'switch_spellcheck'
  - It cycles between English, French, and None
  - It is binded to the key chain ["ctrl+k", "ctrl+s"] and ["ctrl+alt+s"]

TODO 'set_english_email'
  - It enables shellcheck, and sets the dictionary to English
  - It sets the syntax to "Markdown GFM"
  - And ask to save the file

TODO 'set_french_email'
  - It enables shellcheck, and sets the dictionary to French
  - It sets the syntax to "Markdown GFM"
  - And ask to save the file


About:

- *Date:*    2016-09-08
- *Web:*     https://github.com/Naereen/SublimeText3_SwitchDictionary/
- *Author:*  Lilian Besson (C) 2016
- *Licence:* MIT Licence (http://lbesson.mit-license.org)
"""

from __future__ import print_function, division  # Python 2 compatibility if needed

import sublime
import sublime_plugin

from os.path import join


class DisableSpellcheckCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("\nStarting to run the command 'disable_spellcheck' ...")  # DEBUG
        sublime.status_message("Disabling spelling...")

        # 1. Display a message in the status bar
        self.view.set_status("Spelling", "")
        # 2. Disable spell check
        print("Setting 'spell_check' to 'false' ...")  # DEBUG
        self.view.run_command("set_setting", {
            "setting": "spell_check",
            "value": False
        })
        print("Done running the command 'disable_spellcheck' ...")  # DEBUG


path_to_the_dict_en = "Language - English/en_US.dic"
# path_to_the_dict_en = "Dictionaries/en_US.dic"


class EnableEnglishSpellcheckCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("\nStarting to run the command 'enable_english_spellcheck' ...")  # DEBUG
        sublime.status_message("Switching spelling to English...")

        # 1. Load the good dict
        print("Setting 'dictionary' setting to '{}' ...".format(join("Packages", path_to_the_dict_en)))  # DEBUG
        # try:
        self.view.run_command("set_setting", {
            "setting": "dictionary",
            "value": join("Packages", path_to_the_dict_en)
        })
        # except:
        #     self.view.run_command("set_setting", {
        #         "setting": "dictionary",
        #         "value": join("Packages", "Dictionaries/en_US.dic")
        #     })
        # TODO: implement here a smart detection : if "Language - English/en_US.dic" is not here, load "Dictionaries/en_US.dic" instead

        # 2. Enable spell check
        print("Setting 'spell_check' to 'true' ...")  # DEBUG
        self.view.run_command("set_setting", {
            "setting": "spell_check",
            "value": True
        })

        # 3. Display a message in the status bar
        self.view.set_status("Spelling", "English")

        print("Done running the command 'enable_english_spellcheck' ...")  # DEBUG


path_to_the_dict_fr = "Language - French - Français/fr_FR.dic"
# path_to_the_dict_fr = "Dictionaries/French.dic"


class EnableFrenchSpellcheckCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("\nStarting to run the command 'enable_french_spellcheck' ...")  # DEBUG
        sublime.status_message("Switching spelling to French...")

        # 1. Load the good dict
        print("Setting 'dictionary' setting to '{}' ...".format(join("Packages", path_to_the_dict_fr)))  # DEBUG
        # try:
        self.view.run_command("set_setting", {
            "setting": "dictionary",
            "value": join("Packages", path_to_the_dict_fr)
        })
        # except:
        #     self.view.run_command("set_setting", {
        #         "setting": "dictionary",
        #         "value": join("Packages", "Dictionaries/French.dic")
        #     })
        # TODO: implement here a smart detection : if "Language - French - Français/fr_FR.dic" is not here, load "Dictionaries/French.dic" instead

        # 2. Enable spell check
        print("Setting 'spell_check' to 'true' ...")  # DEBUG
        self.view.run_command("set_setting", {
            "setting": "spell_check",
            "value": True
        })

        # 3. Display a message in the status bar
        self.view.set_status("Spelling", "French")

        print("Done running the command 'enable_french_spellcheck' ...")  # DEBUG


class SwitchSpellcheckCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("\nStarting to run the command 'switch_spellcheck' ...")  # DEBUG

        try:
            status = self.view.get_status("Spelling")
        except:
            status = None
        print("Status for key='Spelling' =", status)  # DEBUG

        if not status or status == '':  # Default
            sublime.status_message("Switching spelling from {} to English...".format(status))
            self.view.run_command("enable_english_spellcheck")
        elif status == 'English':
            sublime.status_message("Switching spelling from {} to French...".format(status))
            self.view.run_command("enable_french_spellcheck")
        elif status == 'French':
            sublime.status_message("Switching spelling from {} to None...".format(status))
            self.view.run_command("disable_spellcheck")
        else:
            print("Warning (switch_dicts.py from SwitchDictionary plugin): unknown value for 'status'")  # DEBUG

        print("Done running the command 'switch_spellcheck' ...")  # DEBUG


# End of switch_dicts.py
