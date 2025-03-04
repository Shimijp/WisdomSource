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
    "II Chronicles": "דברי הימים ב",

    # Mishnah
    "Berakhot": "ברכות",
    "Peah": "פאה",
    "Demai": "דמאי",
    "Kilayim": "כלאים",
    "Sheviit": "שביעית",
    "Terumot": "תרומות",
    "Maasrot": "מעשרות",
    "Maaser Sheni": "מעשר שני",
    "Challah": "חלה",
    "Orlah": "ערלה",
    "Bikkurim": "ביכורים",

    # Moed
    "Shabbat": "שבת",
    "Eruvin": "עירובין",
    "Pesachim": "פסחים",
    "Shekalim": "שקלים",
    "Yoma": "יומא",
    "Sukkah": "סוכה",
    "Beitzah": "ביצה",
    "Rosh Hashanah": "ראש השנה",
    "Taanit": "תענית",
    "Megillah": "מגילה",
    "Moed Katan": "מועד קטן",
    "Chagigah": "חגיגה",

    # Nashim
    "Yevamot": "יבמות",
    "Ketubot": "כתובות",
    "Nedarim": "נדרים",
    "Nazir": "נזיר",
    "Sotah": "סוטה",
    "Gittin": "גיטין",
    "Kiddushin": "קידושין",

    # Nezikin
    "Bava Kamma": "בבא קמא",
    "Bava Metzia": "בבא מציעא",
    "Bava Batra": "בבא בתרא",
    "Sanhedrin": "סנהדרין",
    "Makkot": "מכות",
    "Shevuot": "שבועות",
    "Eduyot": "עדויות",
    "Avodah Zarah": "עבודה זרה",
    "Avot": "אבות",
    "Horayot": "הוריות",

    # Kodashim
    "Zevachim": "זבחים",
    "Menachot": "מנחות",
    "Chullin": "חולין",
    "Bechorot": "בכורות",
    "Arakhin": "ערכין",
    "Temurah": "תמורה",
    "Keritot": "כריתות",
    "Meilah": "מעילה",
    "Tamid": "תמיד",
    "Middot": "מידות",
    "Kinnim": "קנים",

    # Taharot
    "Keilim": "כלים",
    "Ohalot": "אוהלות",
    "Negaim": "נגעים",
    "Parah": "פרה",
    "Tahorot": "טהרות",
    "Mikvaot": "מקואות",
    "Niddah": "נדה",
    "Machshirin": "מכשירין",
    "Zavim": "זבים",
    "Tevul Yom": "טבול יום",
    "Yadayim": "ידיים",
    "Uktzin": "עוקצין"
}

hebrew_to_english_mapping = {value: key for key, value in book_name_mapping.items()}