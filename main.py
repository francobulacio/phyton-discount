import re
from typing import final
from bs4 import BeautifulSoup
import requests
import time
import lxml
import smtplib

my_email = 'francobulacio@gmail.com'
password = 'Huqz3snrybwVL3'

product_url1 = "https://www.mercadolibre.com.ar/memoria-ram-8gb-1x8gb-markvision-mvd38192mld-16/p/MLA6121069?pdp_filters=category:MLA3794#searchVariation=MLA6121069&position=5&type=product&tracking_id=241cfc20-ed2d-4dc4-8baf-19cdbfce8abf"
product_url2 = "https://articulo.mercadolibre.com.ar/MLA-906698173-mega-monopatin-con-2-ruedas-de-aluminio-10118-pce-_JM?variation=74701760563#reco_item_pos=1&reco_backend=promotions-sorted-by-score-mla-A&reco_backend_type=low_level&reco_client=home_seller-promotions-recommendations&reco_id=5af685c3-c2fd-4da6-b2a2-66f98a538c0e&c_id=/home/promotions-recommendations/element&c_element_order=2&c_uid=115acbcc-4078-4428-9e5c-53ddfe6438a1"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(product_url2, headers=headers)
ml_web = response.text



soup = BeautifulSoup(ml_web, "lxml")
text = soup.findAll("span", {"class": "price-tag-fraction"})
text = text[0].getText()
price_split = text.split(".")
price_together = price_split[0] + price_split[1]
first_price = int(price_together)
print(first_price)
    

   
soup2 = BeautifulSoup(ml_web, "lxml")
text2 = soup2.findAll("span", {"class": "price-tag-fraction"})
text2 = text2[1].getText()
price_split2 = text2.split(".")
price_together2 = price_split2[0] + price_split2[1]
second_price = int(price_together2)


if second_price < first_price:
    final_price = second_price
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # Encrypts the email if intercepted
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='francobulacio@gmail.com',
            msg=f'Subject:Mercado Libre: Your wish product is now at ${final_price}, previous price ${first_price}'
        )
else:
    final_price = first_price



