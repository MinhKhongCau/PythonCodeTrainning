 item in sql:
#     file_url = f"{GIT_URL_DOWLOAD}{item}"
#     buffer = BytesIO()
#     c = pycurl.Curl()
#     c.setopt(c.URL, file_url)
#     c.setopt(c.WRITEDATA, buffer)
#     c.perform()
#     c.close()

#     print(buffer