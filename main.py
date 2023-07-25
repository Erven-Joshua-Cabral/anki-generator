import yaml
import genanki
import csv
import random
import os
import sys

CONFIG_DIR = os.path.join(os.getcwd(), "conf")
DATA_DIR = os.path.join(os.getcwd(), "data")
OUTPUT_DIR = os.path.join(os.getcwd(), "out")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.yml")
MODEL_ID_FILE = os.path.join(CONFIG_DIR, "model_id.txt")

conf = {}

# Load the YAML configuration file
def load_config():
    with open(CONFIG_FILE, "r") as yml_conf:
        try:
            conf = yaml.safe_load(yml_conf)
        except yaml.YAMLError as exc:
            print(exc)
    return conf


# Generate a model id for this deck if it is not yet existing.
# Else use the model id of the deck.
def get_model_id():
    
    with open(MODEL_ID_FILE, "r+") as s:
        model_id = s.readline().rstrip()

        if not model_id:
            print("No model id detected. Generating a new id for the anki model.")
            model_id = random.randrange(1 << 30, 1 << 31)
            s.write(str(model_id))

    return int(model_id)


# Generate anki notes using the data from the source file and the anki model
def get_source_data(data_source_file, anki_model):
    anki_notes = []
    with open(data_source_file, "r", encoding='utf-8') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=",")

        for row in csv_reader:
            anki_note = genanki.Note(
                model = anki_model,
                fields = [row[0], row[1], row[2], row[3]],
            )
            anki_notes.append(anki_note)

    return anki_notes

def main():
    
    conf = load_config()
    model_id = get_model_id()

    src_file = os.path.join(DATA_DIR, conf['src_filename'])

    if conf == {}:
        print("Config file was not loaded properly! The script will terminate.")
        sys.exit()

    print("Generating anki deck...")

    anki_model = genanki.Model(
        model_id,
        conf['anki_model_name'],
        fields = conf['Fields'],
        templates = [conf['Template']],
        css = conf['Style'],
    )

    anki_notes = get_source_data(src_file, anki_model)
    
    if anki_notes == []:
        print("Unable to generate anki notes properly! The script will terminate.")
        sys.exit()
    
    # Shuffle flashcards
    random.shuffle(anki_notes)

    # Create the actual deck and package
    anki_deck = genanki.Deck(model_id, conf['deck_title'])
    anki_package = genanki.Package(anki_deck)

    # Add each generated card to the anki deck
    for anki_note in anki_notes:
        anki_deck.add_note(anki_note)

    # Save the deck to a file
    anki_package.write_to_file(os.path.join(OUTPUT_DIR, conf['deck_name']))

    print(f"File was generated successfully!\nCreated deck with {len(anki_deck.notes)} flashcards.")

if __name__ == "__main__":
    main()