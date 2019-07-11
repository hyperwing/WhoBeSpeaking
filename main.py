from bs4 import BeautifulSoup

with open("messages.html", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    print( soup.body.find('div', attrs={'class':'from_name'}).text)