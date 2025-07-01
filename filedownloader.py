# Import the 'requests' library to handle HTTP requests
import requests

# Define the URL of the file to be downloaded
url = 'https://download.sysinternal.com/files/PSTools.zip'

# Send a GET request to the URL and allow automatic redirection (if any)
r = requests.get(url, allow_redirects=True)

# Write the downloaded content (binary data) to a local file named 'PSTools.zip'
open('PSTools.zip', 'wb').write(r.content)
