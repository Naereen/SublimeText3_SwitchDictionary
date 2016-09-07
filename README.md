# SublimeText3 SwitchDictionary
It is a tiny [Sublime Text 3]() plugin, not tested on ST 2, that add commands and shortcuts to switch between: no spellcheck, spellcheck for French, and spellcheck for English.

*Note:* it will soon be better, allowing you to define your own list of dictionaries.

## Commands
### `enable_english_spellcheck`
  - It enables shellcheck, and sets the dictionary to *English*
  - [It is binded]() to the key chain <key>ctrl+k, ctrl+e</key>

### `enable_french_spellcheck`
  - It enables shellcheck, and sets the dictionary to *French*
  - [It is binded]() to the key chain <key>ctrl+k, ctrl+f</key>

### `switch_spellcheck`
  - It cycles between *English*, *French*, and *None*
  - [It is binded]() to the key chain <key>ctrl+k, ctrl+s</key> and <key>ctrl+alt+s</key>

### `disable_spellcheck`
  - It disables shellcheck
  - It is NOT binded to any key

----

## Accessing commands through...
### The palette
Search for 

----

## Install
### With [Package Control](https://packagecontrol.io/)
If you have [Package Control](https://packagecontrol.io/) installed in Sublime Text 2/3, just press <key>ctrl+shift+p</key> (Windows, Linux) or <key>cmd+shift+p</key> (OS X) to open the Command Pallete.

Start typing `install` to select `Package Control: Install Package`, then search for `SwitchDictionary` and select it. That's it.

### Manually, with git
You can also install this package manually by entering the Packages directory of Sublime Text 2/3 and issuing on a terminal:

    git clone https://github.com/Naereen/SublimeText3_SwitchDictionary

----

## :boom: TODO
- Publish it !
- Find a nice way to install it locally?

## :hourglass: Future Features
- Be more general: allow users to define manually a list of dictionary (path, and name), and add one command for each dictionary, and make the switch_spellcheck command cycle between them!

----

### :scroll: License
This plugin is published under the terms of the [MIT license](http://lbesson.mit-license.org/) (file [LICENSE.txt](LICENSE.txt)).
© [Lilian Besson](https://github.com/Naereen), 2016.

[![Ask Me Anything](https://img.shields.io/badge/ask%20me-anything-1abc9c.svg)](https://github.com/Naereen/ama)
[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/SublimeText3_SwitchDictionary/README.md?pixel)](https://github.com/Naereen/SublimeText3_SwitchDictionary/)
