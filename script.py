#Web scrapping wit Soup

# 1. Incorporate the necessary libraries
import requests
from bs4 import BeautifulSoup

# 2.Make a request to the website
url = "https://www.portalinmobiliario.com/"

# 3.Keep the respond from the website
response = requests.get(url) # Get the HTML content of the website // request method 

# 4. Verify the status code
if response.status_code == 200:
    print("The request was successful")#delete post verify the status code
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("div", class_="andes-carousel-snapped__slide andes-carousel-snapped__slide--next")
    print(len(products))
    
    
    for product in products:
        title = product.find("span", class_="ui-item__bottom-title")
        if title:
            print(title.text.strip())
            
else:
    print("The request failed with status code:", response.status_code)




