import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/BestOffice-Gaming-Executive-Headrest-Computer/dp/B07KJYY9BD/ref=sr_1_3?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.cXu8MYW9nX1IwoAo1--wPWWFCjcIMpFzSeCUlPNx7f8fvi9viCg27THTSXViJnDRfm4h-6m4u58yIUzGtIfaRc9421druHZzM7HTPoJTxmiyXI7_C6htWpVMclae6U_2X0YHs8oO8ZOFE_EJdd_nz20zOl8flG4mRUo1YwE9C5mfCC3qC6wvm8Ip_xqq7DNKYp_FAuxcnCNgvYYhH_ET4_iHvYewMtwkjb4fyaUM5DpTPE4X07Lv0MpnAzPX6V60AjAwVvo4ZKw9_Hww7qWR3oRv4tKJotd0DH0VSCpzBe8DB3_PFXAFfSTrGhBXoAK4DdxmZUig8ciwFEudk_30fGrcREI69VcvxKnko4KP2bYR2XGvl2HkRuQimZb3-kYqRxDkZh06q3uOJrHxeRItdgAvratw4am87oW_HGrCAHHNWkhzkKVEdyOFlUGTfUTd.e1kqmQjVaVNdRCfXvYHwMxWCLAl7S2fIQDdU76vVTCw&dib_tag=se&keywords=gaming+chairs&pd_rd_r=d8da739d-5da7-48ed-ba57-9cca0a1c5a65&pd_rd_w=mDIay&pd_rd_wg=nflCW&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=7HAAZ1XTEQAQB8MYHYVT&qid=1737669641&sr=8-3"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
EMAIL= "emmanuelfongong10@gmail.com"
PASSWORD = ""

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(EMAIL, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr="emmanuelfongong10@gmail.com",
            to_addrs="robertjones237@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )