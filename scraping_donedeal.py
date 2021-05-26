import smtplib
import requests
import threading
from bs4 import BeautifulSoup
from email.message import EmailMessage

EMAIL_ADDRESS = "email@gmail.com" # Email which will send you new listings
EMAIL_PASSWORD = "xxxxxxxxxxxx" # Password for using the email above


def search_car():
    source = requests.get(
        "https://www.donedeal.ie/cars"
    ).text

    soup = BeautifulSoup(source, "html5lib")

    for add in soup.find_all('li', class_="card-item"):
        try:

            title = add.find("div", class_="card__body").p.text
            engine = list(add.find("ul", class_="card__body-keyinfo"))[1].text
            year = list(add.find("ul", class_="card__body-keyinfo"))[0].text
            added = list(add.find("ul", class_="card__body-keyinfo"))[3].text
            price = add.find("p", class_="card__price").text
            link = add.find("a")['href']
            if added == "0 min":
                msg = EmailMessage()
                msg['Subject'] = "New car in town!"
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = "example@email.com" # Where you wish to send all new listings.
                msg.set_content(f"{title}\n{year}\n{engine}\n{added}\n{price}\n{link}")

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: #This is a set up for Gmail.
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)

        except Exception:
            continue


WAIT_SECONDS = 60


def timer():
    search_car()
    threading.Timer(WAIT_SECONDS, timer).start()


timer()
