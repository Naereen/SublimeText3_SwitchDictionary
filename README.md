# [SublimeText3 SwitchDictionary](https://github.com/Naereen/SublimeText3_SwitchDictionary/) - EARLY STAGE
## WARNING
[This plug-in](https://github.com/Naereen/SublimeText3_SwitchDictionary/) [is still in active development](https://github.com/Naereen/SublimeText3_SwitchDictionary/graphs/commit-activity) and in early stage!

## About
It is a tiny [Sublime Text 3](https://www.sublimetext.com/3) plug-in (not tested on [ST 2](https://www.sublimetext.com/)), that add commands and shortcuts to switch between: no spell-check, spell-check for *French*, and spell-check for *English*.

This plugin also implements a small automatic language checker to detect if the document is in French or in English (and [embeds](https://github.com/Naereen/SublimeText3_SwitchDictionary/tree/master/langdetect/) a more sophisticated one), but the dictionary is loaded only with a keyboard shortcut, it is *not* turned on automatically.

*Note:* It is restricted to only French vs English for now.
I hope it will soon be better, allowing you to define your own list of dictionaries.

## Demo (gif screencast)
![demo of Sublime Text 3 'SwitchDictionary' plugin (gif)](https://raw.githubusercontent.com/Naereen/SublimeText3_SwitchDictionary/master/demo_SublimeText3_SwitchDictionary_plugin.gif)

----

## Commands
### `enable_english_spellcheck`
  - It enables spell-check, and sets the dictionary to *English*
  - [It is associated](Default.sublime-keymap) to the key chain <kbd>ctrl+k, ctrl+e</kbd>

### `enable_french_spellcheck`
  - It enables spell-check, and sets the dictionary to *French*
  - [It is associated](Default.sublime-keymap) to the key chain <kbd>ctrl+k, ctrl+f</kbd>

### `switch_spellcheck`
  - It cycles between *English*, *French*, and *None*
  - [It is associated](Default.sublime-keymap) to the key chain <kbd>ctrl+k, ctrl+s</kbd> and also to <kbd>ctrl+alt+s</kbd> (*s* for *switch*)

### `auto_switch_spellcheck`
  - It uses [`langdetect.detect`](https://github.com/Mimino666/langdetect) to (try to) automatically detect the language of the current file. I also [manually added](https://github.com/Naereen/SublimeText3_SwitchDictionary/commit/cdaeccee0e15f37d2303db4c55aee66ceb6187b2) a small check (with French accents), as `langdetect` is failing on some very small files
  - Right now, the detected language is only used to know if it is French / or not French (English or other language). TODO I need to generalize this
  - It sets to *French* if the file is in French (or as a high probability of being written in French), and sets to *English* otherwise
  - [It is associated](Default.sublime-keymap) to <kbd>ctrl+alt+a</kbd> (*a* for *auto*)
  - Warning: it requires the current file (edited file) to be saved on the disk, as it uses the content of the file to [guess the language](https://github.com/Mimino666/langdetect#basic-usage)

### `disable_spellcheck`
  - It simply disables the spell-check
  - It is NOT associated to any key (*tip:* use the default command, associated to <kbd>F6</kbd> by default)

----

## Accessing commands through...
### :notebook: The *Command Palette* !
Press <kbd>ctrl+shift+p</kbd> (Windows, Linux) or <kbd>cmd+shift+p</kbd> (OS X) to open the [*Command Palette*](SwitchDictionary.sublime-commands), and then search for:

 - `Switch Dictionary: disable (None)`,
 - `Switch Dictionary: to English`,
 - `Switch Dictionary: to French`,
 - `Switch Dictionary: None ↔ French ↔ English`.
 - `Auto Switch Dictionary (guess)`.

### :mouse: The *Encoding Menu* !
In the status bar, you should have a menu showing the encoding of the current file (by default it is `UTF-8`).
Click on [the menu](Encoding.sublime-menu), and you can *click* on:

 - `Switch Dictionary – Disable (None)`
 - `Switch Dictionary – to English`
 - `Switch Dictionary – to French`
 - `Switch Dictionary – None ↔ French ↔ English`
 - `Auto Switch Dictionary (guess)`

### :musical_keyboard: *Shortcuts* !
[By default](Default.sublime-keymap), the following shortcuts are available

 - <kbd>ctrl+k, ctrl+e</kbd> : `Switch Dictionary – to English`
 - <kbd>ctrl+k, ctrl+f</kbd> : `Switch Dictionary – to French`
 - <kbd>ctrl+k, ctrl+s</kbd> or <kbd>ctrl+alt+s</kbd> : `Switch Dictionary – None ↔ French ↔ English`
 - <kbd>ctrl+alt+a</kbd> : `Auto Switch Dictionary (guess)`

----

## :question: How to install it ?
### :ok_hand: With [Package Control](https://packagecontrol.io/)
If you have [Package Control](https://packagecontrol.io/) installed in Sublime Text 2/3, just press <kbd>ctrl+shift+p</kbd> (Windows, Linux) or <kbd>cmd+shift+p</kbd> (OS X) to open the *Command Palette*.

1. Start typing `install` to select `Package Control: Install Package`,
2. Then search for `SwitchDictionary` and select it. That's it!

> - FIXME *NOT YET !* I am waiting for [this pull request](https://github.com/wbond/package_control_channel/pull/5867) to be included.
> - The package will soon be available [on packagecontrol.io](https://packagecontrol.io/SwitchDictionary)

[![Package Control total downloads](https://img.shields.io/packagecontrol/dt/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)
[![Package Control month downloads](https://img.shields.io/packagecontrol/dm/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)
[![Package Control week downloads](https://img.shields.io/packagecontrol/dw/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)
[![Package Control day downloads](https://img.shields.io/packagecontrol/dd/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)

### :floppy_disk: Manually, with [git](https://git-scm.com/)
You can also install this package manually by entering the Packages directory of Sublime Text 3 (through the menu: "Preferences" > "Browse packages"), and issuing this command on a terminal:

```bash
cd ~/.config/sublime-text-3/Packages/  # adapt the path on Windows or Mac OS X
git clone https://github.com/Naereen/SublimeText3_SwitchDictionary
```

### Check it
You can check it was well installed by hitting <kbd>ctrl+k, ctrl+s</kbd> (it should enable English spell checking).

----

## :boom: [TODO !](https://github.com/Naereen/SublimeText3_SwitchDictionary/projects/1)
- [X] Test it on another laptop : DONE on another Linux laptop
- [ ] Test it on Mac OS X and/or Windows
- [X] Implement a smart detection, to know if a file is in French or in English
- [ ] Be more general, allow a user to define his own favorite dictionaries
- [ ] Finish it completely
- [ ] Include a second screencast showing the "automatic language detection" feature (new in [v0.0.3](https://github.com/Naereen/SublimeText3_SwitchDictionary/releases/tag/v0.0.3))
- [ ] Publish it on [Package Control](https://packagecontrol.io/) ! XXX I am waiting for [this pull request](https://github.com/wbond/package_control_channel/pull/5867) to be included.

## :hourglass: [Future Features](https://github.com/Naereen/SublimeText3_SwitchDictionary/projects/1)
- Be more general: allow users to define manually a list of dictionary (path, and name), and add one command for each dictionary, and make the switch_spellcheck command cycle between them! XXX Use the [ST2 SwitchLanguage plugin](https://packagecontrol.io/packages/SwitchLanguage) ?

----

## :scroll: License ? [![GitHub license](https://img.shields.io/github/license/Naereen/SublimeText3_SwitchDictionary.svg)](https://github.com/Naereen/SublimeText3_SwitchDictionary/blob/master/LICENSE)
This plug-in is published under the terms of the [MIT license](http://lbesson.mit-license.org/) (file [LICENSE.txt](LICENSE.txt)),
© [Lilian Besson](https://GitHub.com/Naereen), 2016.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/SublimeText3_SwitchDictionary/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/SublimeText3_SwitchDictionary/README.md?pixel)](https://GitHub.com/Naereen/SublimeText3_SwitchDictionary/)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-for-st3](https://img.shields.io/badge/Made%20for-SublimeText3-green.svg)](https://www.sublimetext.com/3dev)

[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
