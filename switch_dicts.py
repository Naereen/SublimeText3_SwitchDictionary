#! /usr/bin/env python3
# -*- coding: utf-8; mode: python -*-
""" Tiny SublimeText3 plugin to add these commands:

'disable_spellcheck'
  - It disables shellcheck
  - It is NOT binded to any key (use F6 instead)

'enable_english_spellcheck'
  - It enables shellcheck and sets the dictionary to English
  - It is binded to the key chain ["ctrl+k", "ctrl+e"]

'enable_french_spellcheck'
  - It enables shellcheck and sets the dictionary to French
  - It is binded to the key chain ["ctrl+k", "ctrl+f"]

'switch_spellcheck'
  - It cycles between English, French, and None
  - It is binded to the key chain ["ctrl+k", "ctrl+s"] and ["ctrl+alt+s"]

'auto_switch_spellcheck'
  - It guesses the more probable language (between French and English)
  - It sets the dictionary to English or French, or English by default if it fails?
  - It is binded to the ["ctrl+alt+a"]

TODO 'set_english_email'
  - It enables shellcheck, and sets the dictionary to English
  - It sets the syntax to "Markdown GFM"
  - And ask to save the file ?

TODO 'set_french_email'
  - It enables shellcheck, and sets the dictionary to French
  - It sets the syntax to "Markdown GFM"
  - And ask to save the file ?


About:

- *Date:*    2016-11-07
- *Version:* 0.0.3
- *Web:*     https://github.com/Naereen/SublimeText3_SwitchDictionary/
- *Author:*  Lilian Besson (C) 2016
- *Licence:* MIT Licence (http://lbesson.mit-license.org)
"""

# 1. Import requirements
from __future__ import print_function  # Python 2 compatibility, if needed

import sublime
import sublime_plugin

import sys
import os.path
import codecs  # Should not be used


# Make sure nothing gets broken even if the package langdetect is not available
# Note: It comes from https://github.com/Mimino666/langdetect
try:
    from .langdetect import detect  # relative local import
    # print("Success when importing 'detect' from local 'langdetect' (coming from https://github.com/Mimino666/langdetect) ...")   # DEBUG
except ImportError:
    try:
        # Find out the exact path of the current file
        PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))
        # To add it to the path, so the package 'langdetect' is available
        sys.path.insert(0, PLUGIN_DIR)
        from langdetect import detect
        # Should be fine now?
        # print("Success when importing 'detect' from 'langdetect' (coming from https://github.com/Mimino666/langdetect) ...")   # DEBUG
    except ImportError:
        def detect(*args):
            return "en"
    print("[ERROR] Failed to import langdetect : it will always detect English, by default.")
    print("Are you sure you have installed the SwitchDictionary plugin from packagecontrol.io or from GitHub ?")  # DEBUG


# XXX List of French accents, used for the manual detection of French language
# Ref: https://fr.wikipedia.org/wiki/Diacritiques_utilis%C3%A9s_en_fran%C3%A7ais
french_accents = "àâäéèêëïîôöùûüÿçæœÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇÆŒ"
# Minimum number of these French accents before the file is considered to be written in French
MIN_NUMBER_OF_FRENCH_ACCENT = 3


# 2. Utility functions
def spell_check(self, b):
    """ Set the 'spell_check' setting to the Boolean b (True or False).
    """
    print("Setting 'spell_check' to '%s' ..." % b)  # DEBUG
    self.view.run_command("set_setting", {
        "setting": "spell_check",
        "value": b
    })


def set_setting_dictionary(self, path_to_dict):
    """ Set the 'dictionary' setting to the Boolean path 'path_to_dict'.
    """
    print("Setting 'dictionary' setting to '{}' ...".format(
        os.path.join("Packages", path_to_dict)
    ))  # DEBUG
    self.view.run_command("set_setting", {
        "setting": "dictionary",
        "value": os.path.join("Packages", path_to_dict)
    })


# 3. sublime_plugin.TextCommand classes : commands !

class DisableSpellcheckCommand(sublime_plugin.TextCommand):
    """ TextCommand for ST3, disabling the spell check. """
    def run(self, edit):
        print("\nStarting to run the command 'disable_spellcheck' ...")  # DEBUG
        sublime.status_message("Disabling spelling...")

        # 1. Display an empty message in the status bar
        self.view.set_status("Spelling", "")

        # 2. Disable spell check
        spell_check(self, False)

        print("Done running the command 'disable_spellcheck' ...")  # DEBUG


# path_to_the_dict_en = os.path.join("Language - English", "en_US.dic")
path_to_the_dict_en = os.path.join("Dictionaries", "English (American).dic")


def set_english(self):
    """ Small function to set the dictionary to English and enable spell check."""
    self.view.run_command("set_setting", {
        "setting": "dictionary",
        "value": os.path.join("Packages", path_to_the_dict_en)
    })
    spell_check(self, True)


class EnableEnglishSpellcheckCommand(sublime_plugin.TextCommand):
    """ TextCommand for ST3, enabling the spell check to 'English'. """
    def run(self, edit):
        print("\nStarting to run the command 'enable_english_spellcheck' ...")  # DEBUG
        sublime.status_message("Switching spelling to English...")

        # 1. Load the good dict
        print("Setting 'dictionary' setting to '{}' ...".format(os.path.join("Packages", path_to_the_dict_en)))  # DEBUG
        # try:
        # self.view.run_command("set_setting", {
        #     "setting": "dictionary",
        #     "value": os.path.join("Packages", path_to_the_dict_en)
        # })
        # except:
        #     self.view.run_command("set_setting", {
        #         "setting": "dictionary",
        #         "value": os.path.join("Packages", "Dictionaries", "en_US.dic")
        #     })
        # TODO: implement here a smart detection : if "Language - English/en_US.dic" is not here, load "Dictionaries/en_US.dic" instead

        set_english(self)

        # 2. Enable spell check
        # spell_check(self, True)

        # 3. Display a message in the status bar
        self.view.set_status("Spelling", "English")

        print("Done running the command 'enable_english_spellcheck' ...")  # DEBUG


# path_to_the_dict_fr = os.path.join("Language - French - Français", "fr_FR.dic")
path_to_the_dict_fr = os.path.join("Dictionaries", "French.dic")


def set_french(self):
    """ Small function to set the dictionary to French and enable spell check."""
    self.view.run_command("set_setting", {
        "setting": "dictionary",
        "value": os.path.join("Packages", path_to_the_dict_fr)
    })
    spell_check(self, True)


class EnableFrenchSpellcheckCommand(sublime_plugin.TextCommand):
    """ TextCommand for ST3, enabling the spell check to 'French'. """
    def run(self, edit):
        print("\nStarting to run the command 'enable_french_spellcheck' ...")  # DEBUG
        sublime.status_message("Switching spelling to French...")

        # 1. Load the good dict
        print("Setting 'dictionary' setting to '{}' ...".format(os.path.join("Packages", path_to_the_dict_fr)))  # DEBUG
        # try:
        # self.view.run_command("set_setting", {
        #     "setting": "dictionary",
        #     "value": os.path.join("Packages", path_to_the_dict_fr)
        # })
        # except:
        #     self.view.run_command("set_setting", {
        #         "setting": "dictionary",
        #         "value": os.path.join("Packages", "Dictionaries", "French.dic")
        #     })
        # TODO: implement here a smart detection : if "Language - French - Français/fr_FR.dic" is not here, load "Dictionaries/French.dic" instead

        set_french(self)

        # 2. Enable spell check
        # spell_check(self, True)

        # 3. Display a message in the status bar
        self.view.set_status("Spelling", "French")

        print("Done running the command 'enable_french_spellcheck' ...")  # DEBUG


class SwitchSpellcheckCommand(sublime_plugin.TextCommand):
    """ TextCommand for ST3, switching between 'English', 'French' and None spell check. """
    def run(self, edit):
        print("\nStarting to run the command 'switch_spellcheck' ...")  # DEBUG

        try:
            status = self.view.get_status("Spelling")
            if status == '':
                status = None
        except:
            status = None
        print("Status for key='Spelling' =", status)  # DEBUG

        if not status or status == '':  # Default
            sublime.status_message("Switching spelling from {} to English...".format(status))
            # self.view.run_command("enable_english_spellcheck")
            set_english(self)
            self.view.set_status("Spelling", "English")
        elif status == 'English':
            sublime.status_message("Switching spelling from {} to French...".format(status))
            # self.view.run_command("enable_french_spellcheck")
            set_french(self)
            self.view.set_status("Spelling", "French")
        elif status == 'French':
            sublime.status_message("Switching spelling from {} to None...".format(status))
            # self.view.run_command("disable_spellcheck")
            spell_check(self, False)
            self.view.set_status("Spelling", "")
        else:
            print("Warning (switch_dicts.py from SwitchDictionary plugin): unknown value for 'status'")  # DEBUG

        print("Done running the command 'switch_spellcheck' ...")  # DEBUG


class AutoSwitchSpellcheckCommand(sublime_plugin.TextCommand):
    """ TextCommand for ST3, automatically switching between 'English', 'French' and None spell check. """
    def run(self, edit):
        print("\nStarting to run the command 'auto_switch_spellcheck' ...")  # DEBUG

        # 1. get full content, 'content' of the current file, a unicode Python string
        # 2. run detect(content), gets language code
        # 3. XXX currently, if it is 'fr', sets to French, otherwise sets to English
        detection_success = True
        content_of_current_file = ''
        try:
            # FIXED read the file as UTF-8 to give a unicode string
            try:
                with open(self.view.file_name(), 'r') as current_file:
                    print("I am reading the content of the current file, '%s', with open() ..." % current_file.name)
                    content_of_current_file = ''.join(current_file.readlines())
                detected_language = detect(content_of_current_file)
            except:
                with codecs.open(self.view.file_name(), 'r') as current_file:
                    print("I am reading the content of the current file, '%s', with codecs.open() ..." % current_file.name)
                    content_of_current_file = ''.join(current_file.readlines())
                detected_language = detect(content_of_current_file)
            print("I detected that the current file is apparently written in '%s' ..." % detected_language)

            # DONE add manual checks to see if there is some French accents in the text
            if any(c in content_of_current_file for c in french_accents):
                dict_of_present_french_accents = {c: content_of_current_file.count(c) for c in french_accents if c in content_of_current_file}
                nb = sum(dict_of_present_french_accents.values())
                print("But I also manually detected that {} French accent{} present in this text ...".format(nb, "s are" if nb > 1 else " is"))
                print("These accents were found:", dict_of_present_french_accents)
                print("\nSo that's a total of {} French accents ...".format(nb))
                if nb > MIN_NUMBER_OF_FRENCH_ACCENT:
                    detected_language = 'fr'
        except Exception as e:                 # DEBUG
            # print("[DEBUG] Exception e =", e)  # DEBUG
            # print(sys.exc_info())              # DEBUG
            # import traceback                   # DEBUG
            # print(traceback.format_exc())      # DEBUG
            detected_language = 'en'
            detection_success = False
            print("[ERROR] I failed to open, read or detect the language, using 'en', default language is English ...")

        if detection_success and detected_language == 'fr':
            sublime.status_message("Switching spelling to French (guessed)...")
            # self.view.run_command("enable_french_spellcheck")  # XXX not using run_command anymore
            self.view.set_status("Spelling", "French")
            set_french(self)
        elif detection_success and detected_language != 'en':
            # FIXME implement this in general!
            print("[ERROR] I detected that the current file is in '%s', but I don't know how to set spell check for this language." % detected_language)
            print("==> Do it manually !")
            sublime.status_message("Switching spelling to English (failure, non supported language)...")
            # self.view.run_command("enable_english_spellcheck")  # XXX not using run_command anymore
            set_english(self)
            self.view.set_status("Spelling", "English")
        elif detection_success and detected_language == 'en':
            sublime.status_message("Switching spelling to English (guessed)...")
            # self.view.run_command("enable_english_spellcheck")  # XXX not using run_command anymore
            set_english(self)
            self.view.set_status("Spelling", "English")
        else:
            sublime.status_message("Switching spelling to English (default)...")
            # self.view.run_command("enable_english_spellcheck")  # XXX not using run_command anymore
            set_english(self)
            self.view.set_status("Spelling", "English")

        print("Done running the command 'auto_switch_spellcheck' ...")  # DEBUG


# End of switch_dicts.py
