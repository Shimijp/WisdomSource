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
            raise ValueError(f"Invalid Hebrew letter: {letter}")

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


book_name_mapping = {
    # Torah
    "Genesis": "בראשית",
    "Exodus": "שמות",
    "Leviticus": "ויקרא",
    "Numbers": "במדבר",
    "Deuteronomy": "דברים",

    # Nevi'im
    "Joshua": "יהושע",
    "Judges": "שופטים",
    "I Samuel": "שמואל א",
    "II Samuel": "שמואל ב",
    "I Kings": "מלכים א",
    "II Kings": "מלכים ב",
    "Isaiah": "ישעיהו",
    "Jeremiah": "ירמיהו",
    "Ezekiel": "יחזקאל",
    "Hosea": "הושע",
    "Joel": "יואל",
    "Amos": "עמוס",
    "Obadiah": "עובדיה",
    "Jonah": "יונה",
    "Micah": "מיכה",
    "Nahum": "נחום",
    "Habakkuk": "חבקוק",
    "Zephaniah": "צפניה",
    "Haggai": "חגי",
    "Zechariah": "זכריה",
    "Malachi": "מלאכי",

    # Ketuvim
    "Psalms": "תהילים",
    "Proverbs": "משלי",
    "Job": "איוב",
    "Song_of_Songs": "שיר השירים",
    "Ruth": "רות",
    "Lamentations": "איכה",
    "Ecclesiastes": "קהלת",
    "Esther": "אסתר",
    "Daniel": "דניאל",
    "Ezra": "עזרא",
    "Nehemiah": "נחמיה",
    "I Chronicles": "דברי הימים א",
    "II Chronicles": "דברי הימים ב"
}
hebrew_to_english_mapping = {value: key for key, value in book_name_mapping.items()}
def get_book_in_english(book):
    return hebrew_to_english_mapping[book]


def get_book_in_hebrew(book):
    return book_name_mapping[book]

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
