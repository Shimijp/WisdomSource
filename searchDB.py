import os
import re
import ijson
import json
import unicodedata
from translate import  *
from search import *
########################################
# 1) Utility Functions
########################################

def remove_dashes(text):
    """
    Removes multiple dash-like chars:
      - ASCII hyphen (U+002D)
      - Hebrew maqaf (U+05BE)
      - En dash (U+2013)
      - Em dash (U+2014)
    Add or remove from this pattern as needed.
    """
    return re.sub(r'[\u002D\u05BE\u2013\u2014]', ' ', text)

def remove_diacritics(text):
    """
    Remove all Hebrew diacritics (nikud + cantillation)
    by filtering out combining marks.
    """
    decomposed = unicodedata.normalize('NFD', text)
    filtered = ''.join(
        ch for ch in decomposed
        if not unicodedata.combining(ch)
    )
    return unicodedata.normalize('NFC', filtered)


def find_by_loc(  loc):
    new_loc = loc.split(' ')
    if len(new_loc) <  3:
        return "מראה מקום לא תקין "
    if len(new_loc) == 3:
        book = new_loc[0]
        chapter = new_loc[1]
        verse = new_loc[2]
    if len(new_loc) == 4:
        book = new_loc[0]
        num_book = new_loc[1]
        book = book +' '+ num_book
        chapter = new_loc[2]
        verse = new_loc[3]
    else:
        return "פורמט חיפוש שגוי"
    path = 'Sefaria-Export'
    chapter_num = str((hebrew_to_number(chapter)-1))
    verse_num = str((hebrew_to_number(verse)-1))

    book_english = get_book_in_english(book)
    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    work_name = data.get("work")
                    if work_name == book_english:
                        try:
                            result = data["text"][chapter_num][verse_num]

                            return result
                        except KeyError:
                            return "Chapter or verse not found."


                except Exception as e:
                    print(f"Error reading file '{file_path}': {e}")

def covert_the_name_of_the_lord(name):

        if 'ה\'' in name:
            return name.replace('ה\'', 'יהוה')
        return name



def clean_text(text,  full_lord_name, unify_final_letters=True ):
    """
    Cleans input text by:
      1. Removing bracketed text [ ... ].
      2. Removing dash-like characters.
      3. Removing Hebrew diacritics (nikud + trop).
      4. (Optionally) Normalizing final letters.
      5. Stripping whitespace.
    """
    # Remove bracketed text [ ... ]
    text = re.sub(r'\[.*?\]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove dash-like chars
    text = remove_dashes(text)
    # Remove diacritics
    text = remove_diacritics(text)
    if full_lord_name:
        text = covert_the_name_of_the_lord(text)

    # Unify final letters if desired

    # Strip whitespace
    return text.strip()

########################################
# 2) Main Search Function
########################################

def search_sefaria_export(hebrew_text, full_lord_name,
                          base_path="Sefaria-Export",
                          partial_match=True):

    # Clean the user's search query once
    clean_hebrew_text = clean_text(hebrew_text , full_lord_name)
    matches = []

    # Walk the directory tree
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # ijson: iterative JSON parser
                        parser = ijson.parse(f)

                        # We'll track current path with a stack-like list
                        json_path_stack = []
                        current_key = None

                        # Parse events
                        for prefix, event, value in parser:
                            if event == 'map_key':
                                # We are at a dict key
                                current_key = value

                            elif event in ('start_map', 'start_array'):
                                if current_key is not None:
                                    json_path_stack.append(current_key)
                                    current_key = None
                                else:
                                    # Possibly an array with no preceding map_key
                                    json_path_stack.append('[]')

                            elif event in ('end_map', 'end_array'):
                                if json_path_stack:
                                    json_path_stack.pop()

                            elif event == 'string':

                                # Construct a pseudo-JSON pointer from the stack
                                if current_key is None:
                                    # Might be an array item
                                    json_pointer = '.'.join(json_path_stack + ['[]'])
                                else:
                                    json_pointer = '.'.join(json_path_stack + [current_key])

                                # Clean the text from the JSON
                                cleaned_content = clean_text(value , False)


                                # Perform matching
                                if partial_match and clean_hebrew_text in cleaned_content:

                                        arr = prefix.split('.')
                                        chapter = arr[1]
                                        verse = arr[2]
                                        file_loc = file_path.split('\\')[-2]
                                        matches.append({
                                            'file': file_loc,
                                            'excerpt': value,
                                            'chapter': int(chapter)+1,
                                            'verse': int(verse)+1,


                                        })
                                else:
                                    if cleaned_content == clean_hebrew_text:
                                        if cleaned_content == clean_hebrew_text:

                                            arr = prefix.split('.')
                                            chapter = arr[1]
                                            verse = arr[2]
                                            file_loc = file_path.split('\\')[-2]
                                            matches.append({
                                                'file': file_loc,
                                                'excerpt': value,
                                                'chapter': int(chapter) + 1,
                                                'verse': int(verse) + 1,

                                            })
                                current_key = None

                except Exception as e:
                    print(f"Error reading file '{file_path}': {e}")

    if matches:
        return (get_book_in_hebrew(matches[0]['file']) +" " + number_to_hebrew(matches[0]['chapter'])+" " +
                number_to_hebrew(matches[0]['verse'])+ "\n "+ matches[0]['excerpt'])
    else:
        return ["No matches found."]


########################################
# 3) Example Usage (Optional)
########################################

def main():
    # 1) Provide the Hebrew text snippet you want to search
    hebrew_text = "וַיְסַפֵּ֤ר מֹשֶׁה֙ לְחֹ֣תְנ֔וֹ אֵת֩ כׇּל־אֲשֶׁ֨ר עָשָׂ֤ה ה' לְפַרְעֹ֣ה וּלְמִצְרַ֔יִם עַ֖ל אוֹדֹ֣ת יִשְׂרָאֵ֑ל אֵ֤ת כׇּל הַתְּלָאָה֙ אֲשֶׁ֣ר מְצָאָ֣תַם בַּדֶּ֔רֶךְ וַיַּצִּלֵ֖ם ה' "

    # 2) Provide the path to the directory containing your JSON files
    #    e.g., "Sefaria-Export" or "/path/to/my/sefaria"
    base_path = "Sefaria-Export"

    # 3) Choose partial or exact match
    partial_match = True

    # 4) Perform the search
    results = search_sefaria_export(hebrew_text, True, partial_match=partial_match)

    # 5) Print the results
    if isinstance(results, list):
        if len(results) == 1 and isinstance(results[0], str):
            # Probably "No matches found."
            print(results[0])
        else:
            for match in results:
                print("================================")
                print(f"ספר: {get_book_in_hebrew(match['file'])}")
                print(f"פרק: {number_to_hebrew(match['chapter'])}")
                print(f"פסוק: {number_to_hebrew(match['verse'])}")
                print(f"פסוק מלא: {match['excerpt']}")
    else:
        # In case something unusual is returned
        print(results)


########################################
# 4) Actually run main() if executed directly
########################################

if __name__ == "__main__":
    main()