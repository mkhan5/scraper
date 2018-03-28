import requests
from bs4 import BeautifulSoup

pages=5
url = 'https://lbc.cryptoguru.org/dio/{}'
find_str = '1J8Xv8JZZzQA7Q9sEJrLi4XvUL1vL4Vjec'

found = 0
found_on_url =''
for num in range(1,pages+1):
    print("page number",num)
    response = requests.get(url.format(num), verify=False)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    keys = html_soup.findAll(text=find_str)
    if keys:
        found_on_url = url.format(num)
        found = 1
        break

if found == 0:
    print("Not found")
else:
    print("Found")
    print("Url: ",found_on_url)

