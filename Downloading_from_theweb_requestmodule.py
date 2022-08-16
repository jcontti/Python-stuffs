import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # copy selector in chrome
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')	 
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-ebook/dp/B00WJ049VU') 
print('The price is ' + price)  
#response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#response.status_code # if it OK, the response would be 200

