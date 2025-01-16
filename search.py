import requests
import re
from bs4 import BeautifulSoup
from translate import convert_to_hebrew_source
params = {
        "context": "true",  # Include surrounding text
        "pad": "false",     # No padding
        "commentary": "true"  # Include commentary
    }

def find_by_place(place):

    url = f"https://www.sefaria.org/api/v3/texts/{place}"
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "versions" in data and len(data["versions"]) > 0:
                hebrew_text = data["versions"][0].get("text", "No text available")

                # Clean and normalize the API text
                soup = BeautifulSoup(hebrew_text, "html.parser")
                cleaned_text = soup.get_text().strip()
                return cleaned_text if cleaned_text else "לא נמצאו תוצאות"
        else:
            return f"שגיאה: {str(response.status_code)}"


    except requests.ConnectionError:
        return "No internet connection available."


def find_verse_location(hebrew_text):
    """
    Search Google for the given Hebrew text and return the Sefaria location if found.

    Parameters:
        hebrew_text (str): The Hebrew verse to search for.

    Returns:
        str: The location of the verse if found on Sefaria, or a message if not found.
    """
    google_search_url = "https://www.google.com/search"
    try:
        # Perform a Google search
        response = requests.get(google_search_url, params={"q": hebrew_text}, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code != 200:
            return f"שגיאה: לא ניתן להתחבר לגוגל : {str(response.status_code)}"

        # Parse the search results
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True , limit = 20)

        # Check for Sefaria links and clean the URLs
        for link in links:

            href = link["href"]

            match = re.search(r'/url\?q=([^&]+)', href)
            if match:
                url = match.group(1)  # Extract the actual URL
                print(f"Parsed URL: {url}")  # Debug print to see parsed URLs

                # Check if the URL belongs to Sefaria
                if "sefaria.org" in url:
                    return convert_to_hebrew_source(url.split('/')[-1])  # Convert to Sefaria reference
                if "wikisource.org" in url:
                    return url.split('/')[-1]  # Return WikiSource reference

        return f"לא נמצאו תוצאות בספריה עבור החיפוש: {hebrew_text}"

    except requests.ConnectionError:
        return "No internet connection available."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while connecting to Google: {e}"



