import requests
import time
from bs4 import BeautifulSoup

add_list = []
new_add = []


while True:

    """ Your url here, in this example returning new listings for sharing in Dublin """

    source = requests.get(
        "https://www.daft.ie/sharing/dublin-city?sort=publishDateDesc"
    ).text

    soup = BeautifulSoup(source, "html5lib")

    for add in soup.find_all('li', class_="SearchPage__Result-gg133s-2 itNYNv"):

        try:
            price = add.find("span", class_="TitleBlock__StyledSpan-sc-1avkvav-4 gDBFnc").text
            address = add.find("p", class_="TitleBlock__Address-sc-1avkvav-7 knPImU").text
            room = add.find("p", class_="TitleBlock__CardInfoItem-sc-1avkvav-8 jBZmlN").text
            house = add.find("p", class_="TitleBlock__CardInfoItem-sc-1avkvav-8 bcaKbv").text
            link = add.find("a")['href']
            add_list.append((price, address, room, house, link))

        except Exception:
            pass

    first_add = add_list[0]

    """ Here it just prints all the new listings, but can be set up to send them via email or WhatsApp or
    any other way preferred"""

    if new_add != first_add:
        print(f"{first_add[0]}\n{first_add[1]}\n{first_add[2]}\n{first_add[3]}\nwww.daft.ie{first_add[4]}")
        new_add = first_add

    add_list = []
    time.sleep(60)







