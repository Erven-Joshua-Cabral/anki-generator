# AnkiDeckGenerator

This script generates a customizable Anki deck programatically.

## Requirements
Below is a list of python packages and/or software that should be installed in order to run the script without errors.

- [`genanki`](https://github.com/kerrickstaley/genanki)
- [`yaml`](https://pypi.org/project/PyYAML/)
- [Anki for Desktop](https://apps.ankiweb.net/)

## Config
You can customize your anki deck by editing the config file. The default config file contains the template and fields used for studying japanese. Details about card templates can be found on the official [Anki manual](https://docs.ankiweb.net/templates/intro.html).

## Source data
The source data is a CSV file which contains values for each field, as described in the config file. Each row represents one anki note, and each column in a given row represents the field in the config file in the order in which they were defined. (For example, the first column in the source file represents the first field, 'kanji'. The second column represents the second field, 'kana', and so on.)

