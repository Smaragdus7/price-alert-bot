import requests
# import lxml
from bs4 import BeautifulSoup
import smtplib

SMTP_ADDRESS = ""
EMAIL = ""
PASSWORD = ""

URL = "https://www.amazon.com/Acoustic-WINZZ-Cutaway-Beginner-Starter/dp/B07L62RSHQ/ref=sr_1_54?crid=1JAJJCNRM65M0&keywords=yamaha%2Belectroacoustic%2Bguitar&qid=1658258045&sprefix=yamaha%2Belectroa%2Caps%2C173&sr=8-54&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es-US;q=0.8,es;q=0.7,pt;q=0.6"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
price_as_float = float(price)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 120

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
