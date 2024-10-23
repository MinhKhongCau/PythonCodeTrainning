import pycurl
from io import BytesIO

BASE_URL = 'https://github.com'
GITHUB_FOLDER_URL = 'https://github.com/bbrumm/databasestar/tree/main/sample_databases/sample_db_videogames/sqlserver'

# Function to download HTML content of the page
def fetch_html(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue().decode('utf-8')

# Scrape GitHub page for .sql files
html_content = fetch_html(GITHUB_FOLDER_URL)

print(html_content)
