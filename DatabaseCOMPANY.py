import pycurl
from io import BytesIO
import re
from bs4 import BeautifulSoup
import os

# Install dependencies:
# pip install pycurl beautifulsoup4

BASE_URL = 'https://github.com'
GITHUB_FOLDER_URL = 'https://github.com/Jinglin-LI/SQL-Query/blob/master'
RAW_GITHUB_URL = 'https://raw.githubusercontent.com/Jinglin-LI/SQL-Query/refs/heads/master/'

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

directory_name = "DatabaseCompany"
try:
    os.mkdir(directory_name)
    print(f"Directory{directory_name} make succesfully!!!")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Download each SQL file
for sql_file in sql_files:
    sql_file = f"{directory_name}/{sql_file}"
    file_url = f'{RAW_GITHUB_URL}{sql_file}'
    print(f'Downloading {sql_file} from {file_url}')
    download_file(file_url, sql_file)

print("Download complete.")
