

# noinspection PyUnusedLocal
# skus = unicode string

# ROUND 1 - Our supermarket
# The purpose of this challenge is to implement a supermarket checkout that calculates the total price of a number of items.

# In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. 
# In our store, we'll use individual letters of the alphabet (A, B, C, and so on). 
# Our goods are priced individually. In addition, some items are multi-priced: buy n of them, and they'll cost you y pounds. 
# For example, item A might cost 50 pounds individually, but this week we have a special offer: 
#  buy three As and they'll cost you 130.

# Our price table and offers: 
# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


# Notes: 
#  - For any illegal input return -1

# In order to complete the round you need to implement the following method:
#      checkout(String) -> Integer

# Where:
#  - param[0] = a String containing the SKUs of all the products in the basket
#  - @return = an Integer representing the total checkout value of the items 
skus = 'abcdaabcd'


def checkout(skus):
    # separate string to letters
    skus = list(skus)
    # create a dictionary to store the prices of each letter
    prices = {'A': 50, 'B': 30, 'C': 20, 'D':15}
    # create a dictionary to store the special offers and prices
    offers = {'A': (3,130), 'B': (2,45)}
    # create a dictionary to count occurences of each letter
    # group letters if deal
    basket_ordered = {}
    for sku in skus:
        if sku in basket_ordered:
            basket_ordered[sku] += 1
        else:
            basket_ordered[sku] = 1
    # apply bulk discount where possible
    total = 0
    print (basket_ordered)
    for sku, quantity in basket_ordered:
        if sku in offers:
            offer_req, offer_tot = offers[sku]
            total += (quantity // offer_req[sku])*offer_tot
            total += (quantity%offer_req) * prices[sku]
        else:
            total += quantity*prices[sku]
    print (total)
               

checkout(skus)
   
              

    

    # calc cost of items


    





