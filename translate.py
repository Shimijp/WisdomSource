from sources import *
hebrew_numerals = {
    1: "א", 2: "ב", 3: "ג", 4: "ד", 5: "ה",
    6: "ו", 7: "ז", 8: "ח", 9: "ט",
    10: "י", 20: "כ", 30: "ל", 40: "מ", 50: "נ",
    60: "ס", 70: "ע", 80: "פ", 90: "צ",
    100: "ק", 200: "ר", 300: "ש", 400: "ת"
}
gematria_map = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}


def hebrew_to_number(hebrew_str):
    # Mapping of Hebrew letters to their gematria values


    # Sum the values of the letters in the input string
    total = 0
    for letter in hebrew_str:
        if letter in gematria_map:
            total += gematria_map[letter]
        else:
            return ValueError(f"Invalid Hebrew letter: {letter}")

    return total

def number_to_hebrew(num):
    """
    Convert an integer to Hebrew numerals.

    Parameters:
        num (int): The number to convert.

    Returns:
        str: The Hebrew numeral representation.
    """


    # Handle special cases for 15 and 16
    if num == 15:
        return "ט״ו"
    if num == 16:
        return "ט״ז"

    # Break the number into parts (hundreds, tens, and ones)
    result = ""
    for value, letter in sorted(hebrew_numerals.items(), reverse=True):
        while num >= value:
            result += letter
            num -= value

    return result

def get_english_loc(loc):
    book = ""
    chapter = ""
    verse =""
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
    return  [hebrew_to_english_mapping.get(book, book), hebrew_to_number(chapter),
             hebrew_to_number(verse)]


def get_book_in_english(book):

    return hebrew_to_english_mapping.get(book, book)


def get_book_in_hebrew(book):
    return book_name_mapping.get(book, book)

def convert_to_hebrew_source(english_reference):
    try:
    # Split the reference into components
        parts = english_reference.split(".")
        english_book = parts[0]  # e.g., "Exodus"
        chapter = int(parts[1])  # e.g., 7
        verse = int(parts[2])  # e.g., 15

    # Get the Hebrew book name
        hebrew_book = book_name_mapping.get(english_book, "Unknown Book")

    # Format the Hebrew reference)
        hebrew_reference = f"{hebrew_book} {number_to_hebrew(chapter)}, {number_to_hebrew(verse)}"
        return hebrew_reference

    except (IndexError, ValueError):
        return "פורמט חיפוש שגוית נסה שוב"
