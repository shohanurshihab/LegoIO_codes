import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import time
# Replace this with the URL of the webpage you're working with
url = 'https://ns26njj87sh.dataflightit.com/cart/checkout/sign-in/mmh/loginorguestsuccess'

# Send an HTTP GET request to the webpage and parse its content
response = requests.get(url)
time.sleep(10)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the iframe element containing the PayPal button
iframe = soup.find('iframe', {'allowpaymentrequest': 'allowpaymentrequest'})

if iframe:
    # Extract the src attribute from the iframe
    iframe_src = iframe.get('src')
    
    # Parse the query parameters from the iframe URL
    parsed_url = urlparse(iframe_src)
    query_params = parse_qs(parsed_url.query)
    
    # Extract the PayPal button URL from the query parameters
    paypal_button_url = query_params.get('url', [''])[0]
    
    if paypal_button_url:
        # Now you can use the paypal_button_url for further processing
        print(f"PayPal Button URL: {paypal_button_url}")
    else:
        print("PayPal button URL not found in iframe src.")
else:
    print("No iframe with allowpaymentrequest attribute found on the page.")
