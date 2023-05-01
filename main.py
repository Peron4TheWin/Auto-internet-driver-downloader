import subprocess
import requests
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from tqdm import tqdm
def download_file(url):
    response = requests.get(url, stream=True)
    filename = urlparse(url).path.split('/')[-1]
    file_size = int(response.headers.get('Content-Length', 0))
    progress_bar = tqdm(total=file_size, unit='iB', unit_scale=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            progress_bar.update(len(chunk))
            file.write(chunk)
    progress_bar.close()
    return filename
def cmd(command):
    return subprocess.check_output(command, shell=True).decode('utf-8')
def clear():
    subprocess.call("cls", shell=True)
clear()
print("Searching your drivers")
a=(cmd('powershell "Get-NetAdapter | Select-Object -ExpandProperty InterfaceDescription | ForEach-Object {Get-PnpDevice -Class Net -FriendlyName $_} | Select-Object -ExpandProperty HardwareID"')).split("\n")
b = [s.strip() for s in a]

sorted_list = sorted(b, key=len, reverse=True)
sorted_list = sorted(sorted_list, key=len, reverse=True)
c = sorted_list[1]


url = "https://driverpack.io/api/search"
data = {
    "query": c,
    "limit": 7
}
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)
d=(response.json())
e=(d.get("data")[0].get("link"))
f=f"https://driverpack.io/en{e}?os=windows-10-x64"
response = requests.get(f)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
link_urls = [link.get('href') for link in links]
zip_links = [link for link in link_urls if link.endswith('.zip')]
clear()
print("Descargando drivers")
(download_file(zip_links[0]))
print("succesfully downloaded drivers")
