import pycurl
from io import BytesIO
import re
from bs4 import BeautifulSoup

# Install dependencies:
# pip install pycurl beautifulsoup4

BASE_URL = 'https://github.com'
GITHUB_FOLDER_URL = 'https://github.com/bbrumm/databasestar/tree/main/sample_databases/sample_db_videogames/mysql'
RAW_GITHUB_URL = 'https://raw.githubusercontent.com/bbrumm/databasestar/refs/heads/main/sample_databases/sample_db_videogames/mysql/'

# Function to download HTML content of the page
def fetch_html(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue().decode('utf-8')

# Function to download a specific SQL file
def download_file(file_url, file_name):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, file_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    with open(file_name, 'wb') as f:
        f.write(buffer.getvalue())

# Scrape GitHub page for .sql files
html_content = fetch_html(GITHUB_FOLDER_URL)

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the links to .sql files
sql_files = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.endswith('.sql'):
        sql_files.append(href.split('/')[-1])  # Extract file name

# Download each SQL file
for sql_file in sql_files:
    file_url = f'{RAW_GITHUB_URL}{sql_file}'
    print(f'Downloading {sql_file} from {file_url}')
    download_file(file_url, sql_file)

print("Download complete.")
