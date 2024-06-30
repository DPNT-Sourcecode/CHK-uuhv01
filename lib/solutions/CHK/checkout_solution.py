# CHK_R2
# ROUND 2 - More offers
# The checkout feature is great and our supermarket is doing fine. Is time to think about growth.
# Our marketing teams wants to experiment with new offer types and we should do our best to support them.

# We are going to sell a new item E.
# Normally E costs 40, but if you buy 2 of Es you will get B free. How cool is that ? Multi-priced items also seemed to work well so we should have more of these.

# Our price table and offers: 
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


# Notes: 
#  - The policy of the supermarket is to always favor the customer when applying special offers.
#  - All the offers are well balanced so that they can be safely combined.
#  - For any illegal input return -1

# In order to complete the round you need to implement the following method:
#      checkout(String) -> Integer

# Where:
#  - param[0] = a String containing the SKUs of all the products in the basket
#  - @return = an Integer representing the total checkout value of the items 


def checkout(skus):
    # separate string to letters
    skus = list(skus)

    # create a dictionary to store the prices of each letter
    prices = {'A': 50, 'B': 30, 'C': 20, 'D':15, 'E':50}
    # create a dictionary to store the special offers and prices
    offers = {'A': [(3,130),(5,200)], 'B': (2,45)}
    bogof_offers =  { 'E':(2,'B')}
    # create a dictionary to count occurences of each letter
    # group letters if deal
    basket_ordered = {}
    for sku in skus:
        if sku not in ('A','B','C','D','E'):
            return -1
        if sku in basket_ordered:
            basket_ordered[sku] += 1
        else:
            basket_ordered[sku] = 1
    # apply bulk discount where possible
    total = 0
    for sku, quantity in basket_ordered.items():
        # BOGOF offer calc
        if sku in bogof_offers:
            bogoffs_earned={} 
            bo_offer_req, free_sku = bogof_offers[sku]
            bogoffs_earned[free_sku]= quantity // bo_offer_req
            total += (quantity%bo_offer_req) * prices[sku]
            # deduct skus from basket if in bogof
            for bogoffsku, bogoff_quant in bogoffs_earned.items():
                if bogoffsku in basket_ordered:
                    basket_ordered[bogoffsku] -= bogoff_quant

    # regular offer
    
        if sku in offers:
            for offer_req, offer_tot in offers[sku]:
                if quantity >= offer_req:
                    total += (quantity // offer_req)*offer_price
                    total += (quantity%offer_req) * prices[sku]
    
    # remaining items
        else:

            total += quantity*prices[sku]
    print (total)
    return total
    
    
checkout('B')









