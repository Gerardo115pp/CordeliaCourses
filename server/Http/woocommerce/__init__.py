import requests
import os
from typing import List, Dict

def getEmailOrdersIds(email: str, woo_ck: str=None, woo_sk: str=None) -> List[int]:
    """
        recieves an email an optionally a woocommerce consumer key and secret, if this two are not provided
        then they are excepected to be in the environment variables 'woo_customer_key' and 'woo_customer_secret' respectively.
        
        it does a get request on the orders resource and uses the search parameter to limit the results to the email, 'search=email'.
        then we add all the line_items ids to a list and return the list.
    """
    if woo_ck is None:
        woo_ck = os.environ["woo_consumer_key"]
    if woo_sk is None:
        woo_sk = os.environ["woo_consumer_secret"]
        
    valid_order_statuses = {"completed", "processing"}

    url = f"https://cordeliaruiz.com/wp-json/wc/v3/orders"
    params = {"search": email}
    response = requests.get(url, params=params, auth=(woo_ck, woo_sk))
    if not response.ok:
        print(f"ERROR ON INTERACTION WITH WOOCOMMERCE: {response.status_code} - {response.reason}")
        return []
    
    orders_data = response.json()
    order_ids = []
    for order in orders_data:
        if order["status"] not in valid_order_statuses:
            continue
        order_ids += [li["product_id"] for li in order["line_items"]]
        
    return order_ids
 