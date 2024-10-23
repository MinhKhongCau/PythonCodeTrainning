import pycurl
from io import BytesIO
from bs4 import BeautifulSoup
GIT_URL = "https://github.com/bbrumm/databasestar/tree/main/sample_databases/sample_db_videogames/sqlserver"
GIT_URL_DOWLOAD = "https://raw.githubusercontent.com/bbrumm/databasestar/main/sample_databases/sample_db_videogames/sqlserver/"

# Function to decode html to soup
def decode(html):
    return BeautifulSoup(html.decode("utf-8"), 'html.parser')

# Function to loadlink from string
def feth(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL,url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue()

# Function to download a specific SQL file
def download_file(file_url, file_name):
    print(f'Downloading {file_name} from {file_url}')
    buffer = feth(file_url)
    with open(file_name, 'wb') as f:
        f.write(buffer)

buffer = feth(GIT_URL)
soup = decode(buffer)

sql = []
for link in soup.find_all("a",href=True) :
    href = link["href"]
    if (href.endswith(".sql")):
        href = href.split("/")[-1]
        sql.append(href)
    
for item in sql:
    file_url = f"{GIT_URL_DOWLOAD}{item}"
    download_file(file_url,item)

print("Dowload file sucessfully !!!")