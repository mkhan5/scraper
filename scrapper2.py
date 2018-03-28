import requests
from bs4 import BeautifulSoup



pages=1000
url = 'https://lbc.cryptoguru.org/dio/{}'
find_str = '1J8Xv8JZZzQA7Q9sEJrLi4XvUL1vL4Vjec'
for num in range(1,pages):
    print("page number",num)
    response = requests.get(url.format(num), verify=False)
    #print(response.cookies)
    #print(response.text[:2000])

    html_soup = BeautifulSoup(response.text, 'html.parser')
    keys = html_soup.find_all('pre', class_ = 'keys')
    print(len(keys))
    pre = keys[0]

    spans = pre.find_all('span',recursive=False)
    print(len(spans))

    for span in spans:
        a = span.find_all('a')
        print(a[1])


exit()
