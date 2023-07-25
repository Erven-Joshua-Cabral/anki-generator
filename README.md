# AnkiDeckGenerator

This script generates a customizable Anki deck programatically.

## Requirements
Below is a list of python packages and/or software that should be installed in order to run the script without errors.

- [`genanki`](https://github.com/kerrickstaley/genanki)
- [`yaml`](https://pypi.org/project/PyYAML/)
- [Anki for Desktop](https://apps.ankiweb.net/)
- [Python 3](https://www.python.org/downloads/)

## Config
You can customize your anki deck by editing the config file. The default config file contains the template and fields used for studying japanese. Details about card templates can be found on the official [Anki manual](https://docs.ankiweb.net/templates/intro.html).

## Source data
The source data is a CSV file which contains values for each field, as described in the config file. Each row represents one anki note, and each column in a given row represents the field in the config file in the order in which they were defined. (For example, the first column in the source file represents the first field, 'kanji'. The second column represents the second field, 'kana', and so on.)

## Usage
0. Install the required software and packages
1. Edit the source.csv file and update it with the items that you want to study
2. Edit the config.yml file if necessary (Config file can be used as-is)
3. Run the main.py file
4. The output (.apkg file) will be located in the out directory. Open it using Anki for Desktop to begin studying
